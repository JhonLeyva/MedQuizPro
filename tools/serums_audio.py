#!/usr/bin/env python3
"""Genera serums/audio/tormenta.mp3: 30 s de lluvia y truenos, estéreo, que se repite sin cortes.
Todo el audio se sintetiza (ruido filtrado por FFT circular y envolventes con cola envolvente), así que el final enlaza con el inicio sin salto.
Los truenos caen en TRUENOS (segundos); serums.js sincroniza los relámpagos con esos mismos instantes.  Uso: python3 tools/serums_audio.py"""
import subprocess, os, wave
import numpy as np
SR, DUR = 32000, 30
N = SR * DUR
TRUENOS = [(4.2, 1.0), (9.4, 0.5), (14.0, 0.8), (18.3, 0.45), (22.6, 1.0), (27.0, 0.6)]   # (instante, fuerza): cerca fuerte, lejos suave; separados 4–5 s
rng = np.random.default_rng(2026)
F = np.fft.rfftfreq(N, 1 / SR)

def ruido():
    return rng.standard_normal(N)
def banda(x, lo, hi, pend=2.0):
    X = np.fft.rfft(x); g = np.ones_like(F)
    g *= 1 / (1 + (lo / np.maximum(F, 1e-3)) ** (2 * pend)) if lo else 1
    g *= 1 / (1 + (F / hi) ** (2 * pend)) if hi else 1
    return np.fft.irfft(X * g, N)
def norm(x): return x / (np.max(np.abs(x)) + 1e-9)
def lento(frec, prof, fase=0.0):
    t = np.arange(N) / SR; return 1 - prof + prof * (0.5 + 0.5 * np.sin(2 * np.pi * frec * t + fase))
def onda_periodica(x):  # modulación lenta y periódica (frecuencias múltiplos de 1/30 s para que cierre)
    return x

def lluvia(canal):
    base = norm(banda(ruido(), 900, 9000)) * 0.55                      # siseo general
    fino = norm(banda(ruido(), 3500, 14000)) * 0.25                    # gotas en hojas y tejas
    gotas = np.zeros(N); idx = rng.integers(0, N, size=int(SR * 38))
    np.add.at(gotas, idx, rng.uniform(0.2, 1.0, size=idx.size)); gotas = norm(banda(gotas, 1500, 7500, 1)) * 0.45  # golpeteo de gotas
    mod = lento(4 / DUR, 0.22, canal) * lento(9 / DUR, 0.12, 1.3 + canal)   # rachas de intensidad
    return (base + fino + gotas) * mod
def viento(canal):
    return norm(banda(ruido(), 80, 520, 2)) * 0.30 * lento(3 / DUR, 0.6, 2.0 + canal)
def trueno(t0, fuerza, canal):
    t = (np.arange(N) / SR - t0) % DUR                                   # cola que se enrolla al inicio
    crack = np.exp(-t / 0.05) * (t < 0.6)
    grave = np.exp(-t / 2.4) * (1 - np.exp(-t / 0.25))                   # retumbo que crece y se apaga
    rod = 0.55 + 0.45 * np.sin(2 * np.pi * (2.3 + 0.5 * canal) * t + canal)   # el retumbo «rueda»
    sonido = norm(banda(ruido(), 1500, 9000)) * crack * 0.9 + norm(banda(ruido(), 22, 170, 3)) * grave * rod * 1.5 + norm(banda(ruido(), 120, 700, 2)) * grave * 0.5
    return sonido * fuerza
def pista(canal):
    x = lluvia(canal) * 0.55 + viento(canal) * 0.6
    for t0, f in TRUENOS: x += trueno(t0 + 0.02 * canal, f, canal) * 0.95
    return x
st = np.stack([pista(0), pista(1)], 1)
st = np.tanh(st * 0.9) ; st = st / np.max(np.abs(st)) * 0.89
tmp = "serums/audio/_t.wav"
with wave.open(tmp, "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st * 32767).astype("<i2").tobytes())
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-codec:a", "libmp3lame", "-b:a", "96k", "-metadata", "title=Tormenta en la sierra (sintetizada)", "serums/audio/tormenta.mp3"], check=True)
os.remove(tmp); print("tormenta.mp3", os.path.getsize("serums/audio/tormenta.mp3") // 1024, "KB;", DUR, "s; truenos en", [t for t, _ in TRUENOS])
