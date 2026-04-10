# 와이파이  : 1 << 0 = 1
# 24시간    : 1 << 1 = 2
# 흡연실    : 1 << 2 = 4
# 주차장    : 1 << 3 = 8

value = int(input("매장 특성 : "))

if value >= (1 << 3):
    print("주차장")
    value -= (1 << 3)

if value >= (1 << 2):
    print("흡연실")
    value -= (1 << 2)

if value >= (1 << 1):
    print("24시간")
    value -= (1 << 1)

if value >= (1 << 0):
    print("와이파이")