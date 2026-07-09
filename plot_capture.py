from hantek.driver import HantekDriver
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------
# Настройки
# ----------------------------
SAMPLE_RATE = 1_000_000      # 1 MS/s
DATA_POINTS = 0x2000         # 8192 точек

driver = HantekDriver()

try:
    driver.connect()

    driver.configure(
        sample_rate_index=0x04,
        voltage_range=0x01,
        channels=2,
    )

    ch1, ch2 = driver.capture(DATA_POINTS)

finally:
    driver.close()

# ----------------------------
# Создаем временную ось
# ----------------------------
time_ms = np.arange(len(ch1)) / SAMPLE_RATE * 1000

# ----------------------------
# График
# ----------------------------
plt.figure(figsize=(22, 8))

# CH1
plt.subplot(2, 1, 1)
plt.plot(time_ms, ch1, linewidth=0.7)
plt.title("Hantek 6022BE - Channel 1")
plt.xlabel("Time (ms)")
plt.ylabel("ADC")
plt.grid(True)

# CH2
plt.subplot(2, 1, 2)
plt.plot(time_ms, ch2, linewidth=0.7)
plt.title("Hantek 6022BE - Channel 2")
plt.xlabel("Time (ms)")
plt.ylabel("ADC")
plt.grid(True)

plt.tight_layout()

# сохранить изображение
plt.savefig("capture.png", dpi=200)

print("Изображение сохранено: capture.png")

# показать окно
plt.show()