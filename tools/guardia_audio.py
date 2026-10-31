#!/usr/bin/env python3
"""Genera guardia/audio/{emergencias,uci,consulta}.mp3: tres temas de 30 s, estéreo, sintetizados (sin muestras ni grabaciones), que se repiten sin cortes.
Todo evento cae en un instante fijo del ciclo (constantes de abajo) y la animación de intro_servicio.js usa esos mismos instantes para que los monitores latan con el sonido:
  emergencias  120 BPM · RCP (0–10 s, alarma) → carga del desfibrilador (10–14 s) → descarga a los 14,0 s → ritmo recuperado a 120 /min (latido cada 0,5 s desde los 15,0 s)
  uci          monitor a 78 /min (latido cada 60/78 s) · respiración a 18 /min (cada 30/9 s) · alarma baja a los 22 s · bomba de infusión a los 8 s
  consulta     96 BPM · Cmaj7 → Am7 → Fmaj7 → G6 (12 tiempos cada uno) · arpegio de marimba, pad cálido y bajo suave
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
    st = np.stack(buf, 1); st = np.tanh(st * 1.05); st = st / np.max(np.abs(st)) * 0.9
    tmp = f"guardia/audio/_{nombre}.wav"
    with wave.open(tmp, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype("<i2").tobytes())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-codec:a", "libmp3lame", "-b:a", "112k", "-metadata", f"title={nombre} (sintetizado)", f"guardia/audio/{nombre}.mp3"], check=True)
    os.remove(tmp); print(nombre, os.path.getsize(f"guardia/audio/{nombre}.mp3") // 1024, "KB")
def nuevo(): return [np.zeros(N), np.zeros(N)]

def emergencias():
    b = nuevo(); beat = 0.5
    for k in range(60):
        t = k * beat; n = int(0.3 * SR); tt = np.arange(n) / SR
        add(b, t, np.sin(2 * np.pi * (45 + 90 * np.exp(-tt / 0.03)) * tt) * np.exp(-tt / 0.14) * 1.0)                         # bombo en cada tiempo
        if k % 2 == 1: add(b, t, ruido_filtrado(int(0.2 * SR), 900, 7000) * env(int(0.2 * SR), 0.001, 0.07) * 0.55, 0.9, 1.0)   # caja en 2 y 4
        add(b, t + beat / 2, ruido_filtrado(int(0.08 * SR), 6000, None) * env(int(0.08 * SR), 0.001, 0.025) * 0.22, 0.8, 1.0)   # charles
    raices = [55.0, 43.65, 49.0, 41.2]                                                                                        # bajo: 8.º, cada 2 compases cambia la raíz
    for c in range(15):
        r = raices[(c // 2) % 4]
        for j in range(4): add(b, c * 2 + j * 0.5 + 0.25, sierra(r, 0.22, 0.004, 0.09, 6) * 0.55)
    for t0, f in ((0, 220.0), (8, 174.6), (16, 196.0), (24, 164.8)):                                                          # acordes tensos que crecen
        for m in (1.0, 1.1892, 1.4983): add(b, t0, sierra(f * m, 7.6, 1.8, 3.0, 5) * 0.16, 0.8, 1.0)
    for t0 in (0.0, 2.5, 5.0, 7.5):                                                                                           # alarma de monitor durante la RCP
        for i in range(3): add(b, t0 + i * 0.13, seno(1050, 0.09, 0.004, 0.08) * 0.34, 0.5, 1.0)
    n = int(4.0 * SR); tt = np.arange(n) / SR                                                                                 # carga del desfibrilador: subida de tono 10 → 14 s
    f = 300 * (2600 / 300) ** (tt / 4.0); fase = 2 * np.pi * np.cumsum(f) / SR
    add(b, 10.0, np.sin(fase) * (0.1 + 0.55 * (tt / 4.0)) * (0.85 + 0.15 * np.sin(2 * np.pi * 9 * tt)) * np.minimum(1, (4.0 - tt) / 0.02), 1.0, 0.8)
    add(b, 10.0, ruido_filtrado(n, 800, 9000) * (tt / 4.0) ** 2 * 0.35)
    n = int(0.5 * SR); tt = np.arange(n) / SR
    add(b, 14.0, np.sin(2 * np.pi * (35 + 140 * np.exp(-tt / 0.05)) * tt) * np.exp(-tt / 0.22) * 1.5)                        # descarga
    add(b, 14.0, ruido_filtrado(int(0.25 * SR), 200, 12000) * env(int(0.25 * SR), 0.0005, 0.07) * 1.2)
    for k in range(30): add(b, 15.0 + k * 0.5, seno(1000, 0.1, 0.002, 0.07) * 0.5, 0.55, 1.0)                              # latidos del monitor (ritmo recuperado)
    for t0 in (15.0, 19.0, 23.0, 27.0):                                                                                       # golpes de orquesta al recuperar el ritmo
        for m in (1, 1.5, 2, 3): add(b, t0, sierra(110 * m, 1.1, 0.01, 0.5, 5) * 0.22, 1.0, 0.8)
    reverb(b, 0.14, 0.9); guardar(b, "emergencias")

def uci():
    b = nuevo(); lat = 60 / 78; resp = 30 / 9
    for k in range(39):
        t = k * lat
        add(b, t, seno(880, 0.12, 0.003, 0.09) * 0.5, 0.6, 1.0)                                                               # pitido del monitor (ECG)
        nn = int(0.25 * SR); tt = np.arange(nn) / SR
        add(b, t, np.sin(2 * np.pi * (50 + 40 * np.exp(-tt / 0.04)) * tt) * np.exp(-tt / 0.1) * 0.55)                          # latido grave
    for k in range(9):                                                                                                         # ventilador: inspiración (1,3 s) y espiración (2,0 s)
        t = k * resp; n1 = int(1.3 * SR); r1 = ruido_filtrado(n1, 300, 2500) * np.sin(np.pi * np.arange(n1) / n1) ** 1.5 * 0.5
        add(b, t, r1, 1.0, 0.8); n2 = int(2.0 * SR); tt = np.arange(n2) / SR
        add(b, t + 1.3, ruido_filtrado(n2, 200, 1800) * np.exp(-tt / 0.6) * 0.38, 0.8, 1.0)
        add(b, t, ruido_filtrado(int(0.05 * SR), 2000, 9000) * 0.7, 0.9, 0.9)                                                  # clic de la válvula
        add(b, t, sierra(55, 1.4, 0.4, 0.8, 5) * 0.3)
    for t0, acorde in ((0.0, (110.0, 164.8, 261.6, 329.6)), (15.0, (87.3, 130.8, 220.0, 261.6))):                              # pad: La menor → Fa mayor
        for f in acorde: add(b, t0, sierra(f, 15.5, 3.0, 8.0, 4) * 0.14, 0.9, 1.0)
    for t0 in (3.0, 12.0, 21.0):                                                                                               # notas de piano eléctrico lejanas
        for i, f in enumerate((440.0, 523.3, 659.3)): add(b, t0 + i * 0.5, pluck(f, 1.6, 0.7) * 0.14, 0.7, 1.0)
    for i, f in enumerate((660.0, 880.0)): add(b, 8.0 + i * 0.35, seno(f, 0.3, 0.004, 0.12) * 0.3, 0.4, 1.0)                  # bomba de infusión
    for t0 in (22.0, 22.5, 23.0): add(b, t0, seno(740, 0.2, 0.004, 0.18) * 0.34, 1.0, 0.6); add(b, t0 + 0.2, seno(587, 0.2, 0.004, 0.18) * 0.34, 1.0, 0.6)   # alarma baja
    n = int(6.0 * SR); tt = np.arange(n) / SR; add(b, 24.0, ruido_filtrado(n, 300, 6000) * (tt / 6.0) ** 2.2 * 0.38)          # subida cinematográfica antes de repetir
    reverb(b, 0.16, 1.1); guardar(b, "uci")

def consulta():
    b = nuevo(); beat = 60 / 96
    notas = lambda m: 261.63 * 2 ** (m / 12)
    acordes = [(0, 4, 7, 11), (-3, 0, 4, 7), (-7, -3, 0, 4), (-5, -1, 2, 4)]            # Cmaj7, Am7, Fmaj7, G6
    for c, ac in enumerate(acordes):
        t0 = c * 12 * beat
        for f in ac: add(b, t0, sierra(notas(f - 12), 12 * beat + 1.0, 0.8, 5.0, 4) * 0.11, 0.9, 1.0)                           # pad cálido
        add(b, t0, seno(notas(ac[0] - 24), 1.6, 0.01, 0.8) * 0.5); add(b, t0 + 6 * beat, seno(notas(ac[0] - 24), 1.1, 0.01, 0.5) * 0.4)   # bajo
        for j in range(24):                                                              # arpegio de marimba en corcheas
            m = ac[[0, 1, 2, 3, 2, 1][j % 6]] + (12 if j % 6 in (3, 4) else 0)
            add(b, t0 + j * beat / 2, pluck(notas(m), 0.9, 0.25) * 0.26, 0.6 + 0.4 * (j % 2), 1.0 - 0.4 * (j % 2))
        add(b, t0, pluck(notas(ac[3] + 12), 2.2, 0.9, 1.4) * 0.3)                       # melodía larga
        add(b, t0 + 6 * beat, pluck(notas(ac[2] + 12), 2.2, 0.9, 1.4) * 0.24)
    for k in range(48):
        add(b, k * beat, ruido_filtrado(int(0.06 * SR), 5000, None) * env(int(0.06 * SR), 0.001, 0.02) * 0.07)
        if k % 4 == 0:
            n = int(0.25 * SR); tt = np.arange(n) / SR; add(b, k * beat, np.sin(2 * np.pi * (55 + 40 * np.exp(-tt / 0.04)) * tt) * np.exp(-tt / 0.12) * 0.28)
    reverb(b, 0.24, 1.2); guardar(b, "consulta")

if __name__ == "__main__":
    emergencias(); uci(); consulta()
