#!/usr/bin/env python3
"""Genera guardia/audio/{emergencias,uci,consulta,hospital}.mp3: cuatro ambientes de 30 s, estéreo, sintetizados (sin muestras ni grabaciones), que se repiten sin cortes.
Todo evento cae en un instante fijo del ciclo (constantes de abajo) y la animación de intro_servicio.js usa esos mismos instantes para que los monitores latan con el sonido:
  emergencias  ambiente tenso (cúmulo disonante, latidos que se aceleran, rechinidos) · RCP (0–10 s, alarma a 1 Hz) → carga del desfibrilador (10–14 s) → descarga a los 14,0 s → ritmo recuperado a 120 /min (latido cada 0,5 s desde los 15,0 s)
  uci          ambiente real: monitor a 78 /min (latido cada 60/78 s) y ventilador a 18 /min (cada 30/9 s), camas vecinas, bombas, alarma lejana, aire acondicionado y voces
  consulta     consultorio: aire acondicionado, voces lejanas, teclas, bolígrafo, papel, timbre de sala de espera y puerta
  hospital     pasillo de hospital para la introducción principal: aire, monitores lejanos, pasos, camilla, puertas, megafonía y pulso grave
Los instantes y las colas se enrollan al inicio (convolución y suma circulares): el final enlaza con el comienzo.   Uso: python3 tools/guardia_audio.py"""
import subprocess, os, wave
import numpy as np
SR, DUR = 32000, 30
N = SR * DUR
rng = np.random.default_rng(31102026)
T = np.arange(N) / SR
F = np.fft.rfftfreq(N, 1 / SR)

def add(buf, t0, sig, gl=1.0, gr=1.0):
    i0 = int(round(t0 * SR)) % N; idx = (i0 + np.arange(len(sig))) % N
    np.add.at(buf[0], idx, sig * gl); np.add.at(buf[1], idx, sig * gr)
def env(n, ataque, caida):
    t = np.arange(n) / SR; return np.minimum(1, t / max(ataque, 1e-4)) * np.exp(-t / caida)
def seno(f, d, ataque=0.003, caida=0.08):
    n = int(d * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * f * t) * env(n, ataque, caida)
def ruido_filtrado(n, lo=None, hi=None):
    x = rng.standard_normal(n); X = np.fft.rfft(x); fr = np.fft.rfftfreq(n, 1 / SR); g = np.ones_like(fr)
    if lo: g *= 1 / (1 + (lo / np.maximum(fr, 1e-3)) ** 4)
    if hi: g *= 1 / (1 + (fr / hi) ** 4)
    y = np.fft.irfft(X * g, n); return y / (np.max(np.abs(y)) + 1e-9)
def sierra(f, d, ataque=0.01, caida=0.5, arm=8):
    n = int(d * SR); t = np.arange(n) / SR; y = sum(np.sin(2 * np.pi * f * k * t) / k for k in range(1, arm + 1)); return y * env(n, ataque, caida) * 0.5
def pluck(f, d=0.9, caida=0.28, idx=2.2):   # marimba/campana por modulación de frecuencia
    n = int(d * SR); t = np.arange(n) / SR; m = np.sin(2 * np.pi * f * 2 * t) * idx * np.exp(-t / 0.08)
    return np.sin(2 * np.pi * f * t + m) * env(n, 0.002, caida)
def reverb(buf, mezcla=0.18, cola=1.1):
    n = int(cola * SR); t = np.arange(n) / SR
    for c in (0, 1):
        ir = rng.standard_normal(n) * np.exp(-t / 0.32); ir /= np.sqrt(np.sum(ir ** 2)); ir = np.pad(ir, (0, N - n))
        buf[c] = buf[c] * (1 - mezcla) + np.fft.irfft(np.fft.rfft(buf[c]) * np.fft.rfft(ir), N) * mezcla * 1.6
def guardar(buf, nombre):
    st = np.stack(buf, 1); st = st * (0.13 / np.sqrt(np.mean(st ** 2))); st = np.tanh(st * 1.6); st = st / np.max(np.abs(st)) * 0.85   # volumen medio parejo y transitorios suavizados
    tmp = f"guardia/audio/_{nombre}.wav"
    with wave.open(tmp, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype("<i2").tobytes())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-codec:a", "libmp3lame", "-b:a", "112k", "-metadata", f"title={nombre} (sintetizado)", f"guardia/audio/{nombre}.mp3"], check=True)
    os.remove(tmp); print(nombre, os.path.getsize(f"guardia/audio/{nombre}.mp3") // 1024, "KB")
def nuevo(): return [np.zeros(N), np.zeros(N)]

def murmullo(dur, fuerza=1.0):
    """Voces lejanas sin palabras: ruido con formantes de vocal y modulación silábica (4–6 Hz), con pausas."""
    n = int(dur * SR); t = np.arange(n) / SR; x = np.zeros(n)
    for f, a in ((500, 1.0), (1500, 0.6), (2500, 0.3)):
        r = rng.standard_normal(n); R = np.fft.rfft(r); fr = np.fft.rfftfreq(n, 1 / SR); R *= np.exp(-((fr - f) / (f * 0.25)) ** 2); x += np.fft.irfft(R, n) * a
    sil = np.maximum(0, np.sin(2 * np.pi * (4.2 + 1.3 * np.sin(2 * np.pi * 0.17 * t)) * t)) ** 1.5
    fr = np.clip(np.sin(2 * np.pi * 0.23 * t + rng.uniform(0, 6)) * 2.2, 0, 1)
    return x / (np.max(np.abs(x)) + 1e-9) * sil * fr * fuerza
def clics(b, tiempos, f0=3200, amp=0.2, pan=(1.0, 1.0)):
    for t0 in tiempos: add(b, t0, ruido_filtrado(int(0.012 * SR), f0, 9000) * env(int(0.012 * SR), 0.0004, 0.004) * amp, *pan)
def zumbido(b, nivel=0.05, lo=120, hi=900):
    for c in (0, 1): b[c] += ruido_filtrado(N, lo, hi) * nivel * (0.8 + 0.2 * np.sin(2 * np.pi * (2 / DUR) * T + c))     # aire acondicionado: periódico en 30 s
def pitidos(b, bpm, f, nivel, pan, desfase=0.0, d=0.1):
    n = round(DUR * bpm / 60)
    for k in range(n): add(b, desfase + k * 60 / bpm, seno(f, d, 0.003, d * 0.7) * nivel, *pan)

def emergencias():
    """Ambiente tenso: zumbido grave y disonante, latidos que se aceleran, metales y rechinidos, tinnitus; los hitos (alarma, carga, descarga, ritmo) siguen los de la animación."""
    b = nuevo()
    for f, g in ((36.7, 0.7), (55.0, 0.5), (58.3, 0.42), (82.4, 0.26), (116.5, 0.18)):                                      # cúmulo disonante (segunda menor y trítono)
        n = N; mod = 0.65 + 0.35 * np.sin(2 * np.pi * (3 / DUR) * T + f); y = np.sin(2 * np.pi * f * T) * mod * g * 0.18
        for c, d in ((0, 1.0), (1, 1.004)): b[c] += np.sin(2 * np.pi * f * d * T + 0.7 * np.sin(2 * np.pi * (1 / DUR) * T)) * mod * g * 0.16
    b[0] += ruido_filtrado(N, 30, 180) * 0.16 * (0.7 + 0.3 * np.sin(2 * np.pi * (2 / DUR) * T)); b[1] += ruido_filtrado(N, 30, 180) * 0.16 * (0.7 + 0.3 * np.cos(2 * np.pi * (2 / DUR) * T))   # retumbo
    for k in range(18):                                                                                                    # compresiones: golpes sordos (0–10 s)
        t = k * 0.5454; n = int(0.22 * SR); tt = np.arange(n) / SR
        add(b, t, np.sin(2 * np.pi * (48 + 60 * np.exp(-tt / 0.03)) * tt) * np.exp(-tt / 0.09) * 0.95); add(b, t + 0.012, ruido_filtrado(int(0.04 * SR), 150, 1200) * env(int(0.04 * SR), 0.001, 0.012) * 0.35)
    for k in range(10): add(b, k + 0.25, seno(1100, 0.07, 0.003, 0.05) * 0.32, 0.5, 1.0); add(b, k + 0.4, seno(1100, 0.07, 0.003, 0.05) * 0.32, 0.5, 1.0)     # alarma de monitor, 1 Hz (0–10 s)
    for i, (t0, d) in enumerate(((10.0, 0.62), (10.62, 0.52), (11.14, 0.44), (11.58, 0.38), (11.96, 0.33), (12.29, 0.29), (12.58, 0.26), (12.84, 0.23), (13.07, 0.21), (13.28, 0.2), (13.48, 0.19), (13.67, 0.18))):   # latido que se acelera (10–14 s)
        n = int(0.28 * SR); tt = np.arange(n) / SR; add(b, t0, np.sin(2 * np.pi * (42 + 50 * np.exp(-tt / 0.04)) * tt) * np.exp(-tt / 0.11) * 0.85); add(b, t0 + 0.14, np.sin(2 * np.pi * (38 + 40 * np.exp(-tt / 0.04)) * tt) * np.exp(-tt / 0.09) * 0.55)
    n = int(4.0 * SR); tt = np.arange(n) / SR                                                                               # carga del desfibrilador (10 → 14 s)
    f = 300 * (2600 / 300) ** (tt / 4.0); fase = 2 * np.pi * np.cumsum(f) / SR
    add(b, 10.0, np.sin(fase) * (0.08 + 0.5 * (tt / 4.0)) * (0.85 + 0.15 * np.sin(2 * np.pi * 9 * tt)) * np.minimum(1, (4.0 - tt) / 0.02), 1.0, 0.8)
    add(b, 10.0, ruido_filtrado(n, 800, 9000) * (tt / 4.0) ** 2.4 * 0.3)
    n = int(0.6 * SR); tt = np.arange(n) / SR                                                                               # descarga y vacío posterior
    add(b, 14.0, np.sin(2 * np.pi * (32 + 150 * np.exp(-tt / 0.05)) * tt) * np.exp(-tt / 0.28) * 1.7); add(b, 14.0, ruido_filtrado(int(0.25 * SR), 200, 12000) * env(int(0.25 * SR), 0.0005, 0.07) * 1.2)
    for k in range(30): add(b, 15.0 + k * 0.5, seno(1000, 0.1, 0.002, 0.07) * (0.34 + 0.0 * k), 0.55, 1.0)                  # latidos del monitor (ritmo recuperado)
    for t0, f0, dur in ((1.0, 2200, 9.0), (12.0, 3100, 7.0), (20.5, 1800, 9.0)):                                              # metales y cuerdas que raspan: glissandos agudos disonantes
        n = int(dur * SR); tt = np.arange(n) / SR; fr = f0 * (1 + 0.05 * tt / dur) * (1 + 0.012 * np.sin(2 * np.pi * 5.3 * tt)); add(b, t0, np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.sin(np.pi * tt / dur) ** 2 * 0.045, 0.7, 1.0)
        add(b, t0 + 0.7, np.sin(2 * np.pi * np.cumsum(fr * 1.0595) / SR) * np.sin(np.pi * tt / dur) ** 2 * 0.04, 1.0, 0.7)
    for t0 in (3.0, 17.0, 25.0):                                                                                            # rechinidos metálicos breves
        n = int(1.6 * SR); tt = np.arange(n) / SR; add(b, t0, ruido_filtrado(n, 2500, 8000) * np.sin(np.pi * tt / 1.6) ** 3 * (0.6 + 0.4 * np.sin(2 * np.pi * 23 * tt)) * 0.12, 1.0, 0.6)
    b[0] += np.sin(2 * np.pi * 3800 * T) * 0.012 * (0.5 + 0.5 * np.sin(2 * np.pi * (6 / DUR) * T)); b[1] += np.sin(2 * np.pi * 3830 * T) * 0.012       # tinnitus tenue
    n = int(5.0 * SR); tt = np.arange(n) / SR; add(b, 25.0, ruido_filtrado(n, 400, 7000) * (tt / 5.0) ** 2.2 * 0.22)       # subida final antes de volver a empezar
    reverb(b, 0.2, 1.4); guardar(b, "emergencias")

def uci():
    """Ambiente real de una UCI: varios monitores a distinto ritmo, ventilador, bombas de infusión, alarmas lejanas, aire acondicionado y voces lejanas. El monitor principal (78 /min) y el ventilador (18 /min) son los de la animación."""
    b = nuevo(); lat = 60 / 78; resp = 30 / 9
    zumbido(b, 0.05, 90, 700)
    for c in (0, 1): b[c] += np.sin(2 * np.pi * 60 * T) * 0.01 + np.sin(2 * np.pi * 120 * T) * 0.006
    pitidos(b, 78, 880, 0.5, (0.6, 1.0))                                                                                      # monitor de la cama (animado)
    for k in range(39):
        nn = int(0.25 * SR); tt = np.arange(nn) / SR; add(b, k * lat, np.sin(2 * np.pi * (50 + 35 * np.exp(-tt / 0.04)) * tt) * np.exp(-tt / 0.1) * 0.22)   # latido sordo del monitor
    pitidos(b, 66, 740, 0.16, (1.0, 0.35), 0.31); pitidos(b, 90, 1040, 0.11, (0.3, 1.0), 0.17); pitidos(b, 54, 660, 0.09, (0.9, 0.3), 0.5)   # camas vecinas, más lejos
    for k in range(9):                                                                                                        # ventilador
        t = k * resp; n1 = int(1.3 * SR); r1 = ruido_filtrado(n1, 300, 2600) * np.sin(np.pi * np.arange(n1) / n1) ** 1.5 * 0.55
        add(b, t, r1, 1.0, 0.8); n2 = int(2.0 * SR); tt = np.arange(n2) / SR; add(b, t + 1.3, ruido_filtrado(n2, 200, 1900) * np.exp(-tt / 0.6) * 0.4, 0.8, 1.0)
        add(b, t, ruido_filtrado(int(0.05 * SR), 2000, 9000) * env(int(0.05 * SR), 0.002, 0.02) * 0.4); add(b, t + 1.3, ruido_filtrado(int(0.04 * SR), 1500, 7000) * env(int(0.04 * SR), 0.002, 0.02) * 0.25)
        add(b, t, sierra(48, 1.4, 0.4, 0.8, 4) * 0.12)
    for t0 in (4.0, 11.5, 19.0, 26.5): clics(b, [t0, t0 + 0.9], 1800, 0.15)                                                   # bombas de infusión: engranaje
    for i, f in enumerate((660.0, 880.0, 660.0)): add(b, 8.0 + i * 0.28, seno(f, 0.25, 0.004, 0.1) * 0.28, 0.4, 1.0)         # bomba: fin de infusión
    for t0 in (22.0, 22.5, 23.0): add(b, t0, seno(740, 0.2, 0.004, 0.18) * 0.3, 1.0, 0.6); add(b, t0 + 0.2, seno(587, 0.2, 0.004, 0.18) * 0.3, 1.0, 0.6)   # alarma de prioridad media (lejana)
    for t0 in (14.0, 28.0): add(b, t0, seno(1500, 0.06, 0.002, 0.04) * 0.14, 0.2, 1.0)
    for t0, d in ((2.0, 5.0), (13.0, 6.0), (21.0, 5.5)): add(b, t0, murmullo(d, 0.07), 0.6, 1.0)                              # personal conversando al fondo
    clics(b, [6.2, 6.5, 17.8], 600, 0.18); add(b, 24.5, ruido_filtrado(int(0.6 * SR), 400, 3500) * np.sin(np.pi * np.arange(int(0.6 * SR)) / int(0.6 * SR)) * 0.1)    # puerta y pasos
    reverb(b, 0.2, 0.9); guardar(b, "uci")

def consulta():
    """Consultorio de atención ambulatoria: aire acondicionado suave, voces lejanas, teclas, papel, bolígrafo, un timbre de sala de espera y una puerta."""
    b = nuevo()
    zumbido(b, 0.09, 100, 700)
    for t0, d in ((0.5, 6.0), (9.0, 5.0), (16.0, 6.5), (24.0, 5.0)): add(b, t0, murmullo(d, 0.22), 1.0, 0.7)                  # sala de espera, voces lejanas
    for t0, d in ((3.0, 4.0), (19.0, 3.5)): add(b, t0, murmullo(d, 0.14), 0.4, 1.0)
    teclas = []
    for t0 in (2.0, 10.5, 18.0, 26.0):
        t = t0
        for k in range(rng.integers(10, 18)): t += rng.uniform(0.07, 0.24); teclas.append(t)
    clics(b, teclas, 2500, 0.22, (0.8, 1.0))
    clics(b, [5.4, 5.55, 21.2], 1400, 0.3, (1.0, 0.6))                                                                         # bolígrafo
    for t0 in (7.8, 22.5): add(b, t0, ruido_filtrado(int(0.7 * SR), 1500, 9000) * np.sin(np.pi * np.arange(int(0.7 * SR)) / int(0.7 * SR)) ** 2 * 0.1, 0.7, 1.0)   # papel
    for t0, f1, f2 in ((7.0, 784.0, 659.3), (21.0, 659.3, 523.3)):                                                             # timbre suave de llamado a la sala
        add(b, t0, pluck(f1, 1.6, 0.5, 1.2) * 0.22); add(b, t0 + 0.55, pluck(f2, 2.0, 0.6, 1.2) * 0.22)
    n = int(0.5 * SR); tt = np.arange(n) / SR; add(b, 13.5, np.sin(2 * np.pi * (70 + 40 * np.exp(-tt / 0.02)) * tt) * np.exp(-tt / 0.07) * 0.2); add(b, 13.5, ruido_filtrado(int(0.12 * SR), 200, 1500) * env(int(0.12 * SR), 0.001, 0.04) * 0.12)   # puerta
    for t0 in (13.0, 13.2, 14.4, 14.6): add(b, t0, ruido_filtrado(int(0.05 * SR), 300, 2500) * env(int(0.05 * SR), 0.001, 0.015) * 0.3, 0.5, 1.0)    # pasos
    reverb(b, 0.16, 0.8); guardar(b, "consulta")

def hospital():
    """Introducción principal: pasillo de hospital, aire acondicionado, pitidos de monitores a lo lejos, pasos y ruedas de camilla, puertas automáticas, un aviso de megafonía y un pulso grave cinematográfico."""
    b = nuevo()
    zumbido(b, 0.16, 120, 1400)
    for c in (0, 1): b[c] += ruido_filtrado(N, 25, 140) * 0.1
    for f, g in ((55.0, 0.5), (82.4, 0.3), (110.0, 0.2)):                                                                      # pad grave y cálido
        for c, d in ((0, 1.0), (1, 1.003)): b[c] += np.sin(2 * np.pi * f * d * T) * (0.6 + 0.4 * np.sin(2 * np.pi * (2 / DUR) * T + f)) * g * 0.04
    for k in range(30):                                                                                                       # pulso: latido grave cada segundo
        n = int(0.3 * SR); tt = np.arange(n) / SR; add(b, k * 1.0, np.sin(2 * np.pi * (44 + 36 * np.exp(-tt / 0.04)) * tt) * np.exp(-tt / 0.12) * 0.22); add(b, k * 1.0 + 0.2, np.sin(2 * np.pi * (40 + 30 * np.exp(-tt / 0.04)) * tt) * np.exp(-tt / 0.1) * 0.13)
    pitidos(b, 72, 880, 0.3, (1.0, 0.3), 0.2); pitidos(b, 60, 740, 0.24, (0.3, 1.0), 0.45); pitidos(b, 96, 1000, 0.18, (0.8, 0.8), 0.1)
    clics(b, [3.0 + 0.55 * k for k in range(8)], 500, 0.3, (1.0, 0.6)); clics(b, [20.0 + 0.55 * k for k in range(8)], 500, 0.3, (0.6, 1.0))   # pasos que pasan
    for t0 in (9.0, 24.5):                                                                                                    # camilla con ruedas
        n = int(3.0 * SR); tt = np.arange(n) / SR; add(b, t0, ruido_filtrado(n, 800, 5000) * np.sin(np.pi * tt / 3.0) ** 2 * 0.1 * (0.6 + 0.4 * np.sin(2 * np.pi * 7 * tt)), 1.0 if t0 < 15 else 0.4, 0.4 if t0 < 15 else 1.0)
    for t0 in (6.0, 17.0):                                                                                                    # puerta automática
        n = int(1.0 * SR); tt = np.arange(n) / SR; add(b, t0, ruido_filtrado(n, 300, 3000) * np.sin(np.pi * tt) ** 2 * 0.18)
    for i, f in enumerate((880.0, 698.5)): add(b, 12.0 + i * 0.6, pluck(f, 1.8, 0.7, 1.1) * 0.2)                              # aviso de megafonía
    add(b, 14.0, murmullo(3.0, 0.12), 0.8, 0.8); add(b, 26.0, murmullo(3.0, 0.1), 0.5, 1.0)
    n = int(6.0 * SR); tt = np.arange(n) / SR; add(b, 24.0, ruido_filtrado(n, 300, 6000) * (tt / 6.0) ** 2.4 * 0.16)
    reverb(b, 0.28, 1.6); guardar(b, "hospital")

if __name__ == "__main__":
    emergencias(); uci(); consulta(); hospital()
