from driver import HantekDriver

scope = HantekDriver()

scope.connect()

scope.configure()

ch1, ch2 = scope.capture()

print(len(ch1))
print(min(ch1))
print(max(ch1))

scope.close()