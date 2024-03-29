import simpleaudio as sa
import numpy as np
import matplotlib.pyplot as plt


freq1 = 200
freq2 = 311
freq3 = 411
sample_rate = 48000

sec = 1

t = np.linspace(0, sec, sec * sample_rate)
t2 = np.linspace(0, sec, sec * sample_rate)

note = np.sin(freq1 * t * 2 * np.pi)
audio = note * (2**15 - 1) / np.max(np.abs(note))
audio = audio.astype(np.int16)

note2 = np.sin(freq2 * t * 2 * np.pi)
audio2 = note2 * (2**15 - 1) / np.max(np.abs(note2))
audio2 = audio2.astype(np.int16)

note3 = np.sin(freq3 * t * 2 * np.pi)
audio3 = note3 * (2**15 - 1) / np.max(np.abs(note3))
audio3 = audio3.astype(np.int16)
newnote = np.sin(freq1 * t2 * 2 * np.pi)
newaudio = newnote * (2**15 - 1) / np.max(np.abs(newnote))
newaudio = newaudio.astype(np.int16)

play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
play_obj.wait_done()
play_obj2 = sa.play_buffer(audio2, 1, 2, sample_rate)
play_obj2.wait_done()
play_obj3 = sa.play_buffer(audio3, 1, 2, sample_rate)
play_obj3.wait_done()

plt.plot(t, note, color="blue")
plt.plot(t, note2, color="green")
plt.plot(t, note3, color="red")
plt.show()
