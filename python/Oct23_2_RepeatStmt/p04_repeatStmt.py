# 1 + 2 + 3 + ... + 20 = ?
from random import randint


a = 0
for i in range(1, 21):
    a += i
print(a)
print("---------")

# 1 + 2 + 3 + ... + ? > 100

# 반복문
#   컬렉션 탐색용 : for
#   반복횟수 : for에 range활용해서...
#   반복조건 : while
#       while 조건식:
#                    조건식 만족되면 여기 실행

# 랜덤
b = randint(1, 5)  # 1 ~ 5사이의 랜덤한 정수
print(b)
print("---------")

# 1 ~ 10사이의 랜덤한 정수 10번출력
for i in range(10):
    c = randint(1, 10)
    print(c)
print("---------")

# 1 ~ 10 사이의 랜덤한 정수 4나올때까지 출력
d = randint(1, 10)
print(d)
while d != 4:
    d = randint(1, 10)
    print(d)

# 정수하나 입력받아서 출력
a = int(input("숫자 : "))
print(a)
print("--------")

# 정수하나 입력받아서 출력 - 5라고 쓸때까지
a = int(input("숫자 : "))
print(a)
while a != 5:
    a = int(input("숫자 : "))
    print(a)
