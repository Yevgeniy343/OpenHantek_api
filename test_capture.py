from hantek.driver import HantekDriver


driver = HantekDriver()

try:
    driver.connect()

    driver.configure(
        sample_rate_index=0x04,
        voltage_range=0x01,
        channels=2,
    )

    ch1, ch2 = driver.capture(data_points=0x2000)

    print("CH1 points:", len(ch1))
    print("CH1 min:", min(ch1))
    print("CH1 max:", max(ch1))
    print("CH1 avg:", sum(ch1) / len(ch1))
    print("CH1 first 100:", list(ch1[:100]))

    print("CH2 points:", len(ch2))

finally:
    driver.close()