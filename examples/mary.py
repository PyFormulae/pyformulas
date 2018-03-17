import numpy as np
import pyformulas as pf

def playnote(frequency):
    bitrate = 3.6e5
    duration = 0.05
    num_samples = round(bitrate / 8 * duration)
    wavedata = np.rint(np.sin(np.linspace(0, frequency * duration * 2 * np.pi, num_samples)) * 127.5 + 127.5).astype(
        np.uint8)

    pf.audio.play(wavedata, bitrate=bitrate)

c = 261
d = 294
e = 329
f = 349
g = 392
a = 440
b = 493
C = 523
R = 0

melody = [e, R, d, R, c, R, d, R, e, R, e, R, e, R, d, R, d, R, d, R, e, R, g, R, g, R, e, R, d, R, c, R, d, R, e, R, e, R, e, R, e, R, d, R, d, R, e, R, d, R, c, R, c]

for note in melody:
    playnote(note)