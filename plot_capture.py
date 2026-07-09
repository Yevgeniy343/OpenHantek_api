from hantek.driver import HantekDriver
import matplotlib.pyplot as plt

driver = HantekDriver()

try:
    driver.connect()

    driver.configure(
        sample_rate_index=0x04,
        voltage_range=0x01,
        channels=2,
    )

    ch1, ch2 = driver.capture(data_points=0x2000)

finally:
    driver.close()

plt.figure(figsize=(14, 5))

# Пока рисуем только первый канал
plt.plot(ch1, linewidth=0.8)

plt.title("Hantek 6022BE - Channel 1")
plt.xlabel("Sample")
plt.ylabel("ADC value")
plt.grid(True)

plt.tight_layout()

plt.savefig("capture.png", dpi=150)

print("График сохранен в capture.png")