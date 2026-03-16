from __future__ import annotations

import math
import wave
from pathlib import Path

import numpy as np

OUT = Path('/home/d48reu/science-compiler/hackathon/science_compiler_techno_bed.wav')
SR = 44100
DURATION = 67.5
BPM = 118
BEAT = 60.0 / BPM

n = int(SR * DURATION)
t = np.arange(n) / SR
mix = np.zeros(n, dtype=np.float32)

# Kick: 4-on-the-floor descending sine
for beat_time in np.arange(0, DURATION, BEAT):
    idx0 = int(beat_time * SR)
    length = int(0.22 * SR)
    if idx0 >= n:
        continue
    end = min(n, idx0 + length)
    tt = np.arange(end - idx0) / SR
    env = np.exp(-tt * 18.0)
    freq = 90 - 55 * (tt / 0.22)
    phase = 2 * math.pi * np.cumsum(freq) / SR
    kick = 0.55 * env * np.sin(phase)
    mix[idx0:end] += kick.astype(np.float32)

# Hi-hat: noise bursts on off-beats
rng = np.random.default_rng(7)
noise = rng.normal(0, 1, n).astype(np.float32)
for beat_time in np.arange(BEAT / 2, DURATION, BEAT / 2):
    idx0 = int(beat_time * SR)
    length = int(0.05 * SR)
    if idx0 >= n:
        continue
    end = min(n, idx0 + length)
    tt = np.arange(end - idx0) / SR
    env = np.exp(-tt * 90.0)
    hat = 0.10 * env * noise[idx0:end]
    mix[idx0:end] += hat

# Bass pulse every 2 beats
notes = [55.0, 55.0, 65.41, 49.0, 55.0, 73.42, 65.41, 49.0]
for i, beat_time in enumerate(np.arange(0, DURATION, 2 * BEAT)):
    idx0 = int(beat_time * SR)
    length = int(0.55 * SR)
    if idx0 >= n:
        continue
    end = min(n, idx0 + length)
    tt = np.arange(end - idx0) / SR
    freq = notes[i % len(notes)]
    env = (1 - np.exp(-tt * 18.0)) * np.exp(-tt * 4.8)
    bass = 0.12 * env * np.sin(2 * math.pi * freq * tt)
    bass += 0.04 * env * np.sin(2 * math.pi * freq * 2 * tt)
    mix[idx0:end] += bass.astype(np.float32)

# Soft pad
pad = 0.04 * np.sin(2 * math.pi * 220.0 * t)
pad += 0.03 * np.sin(2 * math.pi * 277.18 * t)
pad += 0.02 * np.sin(2 * math.pi * 329.63 * t)
pad *= (0.65 + 0.35 * np.sin(2 * math.pi * 0.08 * t))
mix += pad.astype(np.float32)

# Gentle sidechain-ish dip on each kick
for beat_time in np.arange(0, DURATION, BEAT):
    idx0 = int(beat_time * SR)
    length = int(0.18 * SR)
    end = min(n, idx0 + length)
    tt = np.arange(end - idx0) / SR
    dip = 1.0 - 0.24 * np.exp(-tt * 15.0)
    mix[idx0:end] *= dip.astype(np.float32)

# Normalize modestly
peak = np.max(np.abs(mix))
if peak > 0:
    mix = 0.85 * mix / peak

pcm = np.int16(np.clip(mix, -1, 1) * 32767)
with wave.open(str(OUT), 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(SR)
    wf.writeframes(pcm.tobytes())

print(OUT)
