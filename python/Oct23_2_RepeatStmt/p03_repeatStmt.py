# 1
# 2
# 3
from math import e
from time import sleep


for i in range(1, 4):
    print(i)
print("-----")
# 1
# 2
# ...
# 10
for i in range(1, 11):
    print(i)
print("------")

for i in range(1, 10, 2):
    print(i)
print("------")

for i in range(9, 0, -2):
    print(i)
print("-------")
# 변수의 기본값 : 변수를 만들기만하고 값 안넣으면?
#   다른 PL : 0/쓰레기값/없음
#   Python : 그런 상황 자체가 나올수 없음

# 1 + 2 + 3+ ... + 10 = ?
a = 0
for i in range(1, 11):
    a += i
print(a)
print("---------")

b = 0
for i in range(1, 20, 2):
    b += i
print(b)
print("---------")

for i in range(1, 10):
    print("2 x %d = %d" % (i, 2 * i))

for dan in range(2, 10):
    for i in range(1, 10):
        print("%d x %d = %d" % (dan, i, dan * i))
print("--------")

for k in range(1, 10):
    for i in range(2, 10):
        print("%d x %d = %d" % (i, k, i * k), end="\t")
    print()
print("---------")

for i in range(5):
    for j in range(5):
        print("ㅋ", end="")
    print()
print("-----")

for i in range(5):
    for j in range(i + 1):
        print("ㅋ", end="")
    print()
print("--------")

for i in range(5):
    for j in range(5 - i):
        print("ㅋ", end="")
    print()
print("---------")

for i in range(5):
    for j in range(i):
        print("  ", end="")
    print("ㅋ")
print("---------")

# for i in range(5):
#     for j in range(i + 1):
#         if i == j :
#             print("ㅋ", end="")
#         else:
#             print("  ", end="")
#     print()
# print("---------")

for i in range(5):
    if (i % 2) == 0:
        s = "ㅋ"
    else:
        s = "ㅎ"
    for j in range(i * 2 + 1):
        print(s, end="")
    print()
