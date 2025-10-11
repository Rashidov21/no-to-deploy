import sounddevice as sd
import numpy as np
import time

samplerate = 44100
window_size = 2048

x = np.fft.rfftfreq(window_size, 1/samplerate)

def detect_instrument(fft_data):
    low = np.mean(fft_data[(x >= 20) & (x < 250)])      # bass
    mid = np.mean(fft_data[(x >= 250) & (x < 2000)])    # mid
    high = np.mean(fft_data[(x >= 2000) & (x < 8000)])  # treble

    # Harmoniklik darajasi (yassi yoki "notali")
    harmonicity = (mid + high) / (low + 1e-6)
    total_energy = np.mean(fft_data)

    # Oddiy qoidalar:
    if total_energy < 0.005:
        return "🌫️ Jimlik"
    if low > mid * 1.5 and low > high:
        return "🥁 Baraban / Bass"
    elif mid > low * 1.2 and high < mid * 1.2:
        return "🎸 Gitara"
    elif high > mid * 1.3:
        return "🎻 Skripka / Yuqori asbob"
    elif total_energy > 0.02 and harmonicity > 1.2:
        return "🎹 Pianino / Akkord"
    else:
        return "🎶 Musiqa (aralash)"

def callback(indata, frames, time, status):
    data = indata[:, 0]
    if len(data) < window_size:
        data = np.pad(data, (0, window_size - len(data)))
    fft_data = np.abs(np.fft.rfft(data))
    fft_data = fft_data / np.max(fft_data) if np.max(fft_data) > 0 else fft_data
    label = detect_instrument(fft_data)
    print(label)

with sd.InputStream(callback=callback, channels=1, samplerate=samplerate, blocksize=window_size):
    print("🎧 Real-time instrument detection (no AI)... Ctrl+C to stop")
    while True:
        time.sleep(0.5)
