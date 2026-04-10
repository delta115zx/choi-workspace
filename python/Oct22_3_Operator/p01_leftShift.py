# 와이파이  : 1 << 0 = 1
# 24시간    : 1 << 1 = 2
# 흡연실    : 1 << 2 = 4
# 주차장    : 1 << 3 = 8

value = int(input("매장 특성 : "))

a = value / 8
if int(a) == 1:
    print("주차장")
value %= 8

a = value / 4
if int(a) == 1:
    print("흡연실")
value %= 4

a = value / 2
if int(a) == 1:
    print("24시간")
value %= 2

a = value
if int(a) == 1:
    print("와이파이")


# 1
# 와이파이

# 2
# 24시간

# 13
# 와이파이
# 흡연실
# 주차장
