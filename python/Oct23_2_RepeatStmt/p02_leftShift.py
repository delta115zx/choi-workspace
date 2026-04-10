# 와이파이  : 1 << 0 = 1
# 24시간    : 1 << 1 = 2
# 흡연실    : 1 << 2 = 4
# 주차장    : 1 << 3 = 8
# 놀이방
# 충전기

value = int(input("매장 특성 : "))

option = ["와이파이", "24시간", "흡연실", "주차장"]

for i in range(len(option) - 1, -1, -1):
    if value >= (1 << i):
        print(option[i])
        value -= 1 << i
