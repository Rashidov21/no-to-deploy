import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

samplerate = 44100
window_size = 2048

plt.ion()
fig, ax = plt.subplots()
x = np.fft.rfftfreq(window_size, 1/samplerate)
line, = ax.semilogx(x, np.zeros_like(x))
ax.set_xlim(20, 20000)
ax.set_ylim(0, 1)
ax.set_title("🎶 Real-time Frequency Spectrum")
ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Magnitude")


fft_data = np.zeros_like(x)

def callback(indata, frames, time, status):
    global fft_data
    if status:
        print(status)
    data = indata[:, 0]
    if len(data) < window_size:
        pad = np.zeros(window_size - len(data))
        data = np.concatenate((data, pad))
    else:
        data = data[:window_size]
    new_fft = np.abs(np.fft.rfft(data))
    fft_data = new_fft / np.max(new_fft) if np.max(new_fft) > 0 else new_fft


with sd.InputStream(callback=callback, channels=1, samplerate=samplerate, blocksize=window_size):
    print("📊 Real-time spectrum visualization... (Ctrl+C to stop)")
    while True:
        line.set_ydata(fft_data)   
        plt.pause(0.01)           
