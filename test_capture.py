from hantek.driver import HantekDriver
from collections import Counter

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

    print("CH1 unique values:", len(set(ch1)))
    print("CH1 unique:", sorted(set(ch1)))

    print("CH2 points:", len(ch2))
    print("CH2 min:", min(ch2))
    print("CH2 max:", max(ch2))
    print("CH2 avg:", sum(ch2) / len(ch2))
    print("CH2 unique values:", len(set(ch2)))
    print("CH2 unique:", sorted(set(ch2)))

    print("CH1 first 100:", list(ch1[:100]))

    counter = Counter(ch1)

    print("\nСамые частые значения CH1:")

    for value, count in counter.most_common(20):
        print(f"{value}: {count}")

finally:
    driver.close()