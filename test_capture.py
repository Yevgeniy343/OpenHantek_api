from hantek.driver import HantekDriver

driver = HantekDriver()

try:
    driver.connect()

    # Пока НЕ вызываем configure()

    ch1, ch2 = driver.capture(data_points=0x2000)

    print("CH1:", len(ch1))
    print("CH2:", len(ch2))

    print(ch1[:20])

finally:
    driver.close()