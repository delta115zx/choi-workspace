# 로또 번호 자동
# 1 ~ 45사이의 중복없게 랜덤한 숫자 6개

from random import randint, sample


# lotto = sample(range(1, 46), 6)
# print(lotto)

b = []
while True:
    c = randint(1, 45)
    b.append(c)
    b = set(b)
    b = list(b)
    if len(b) == 6:
        break
print(b)
print("--------")


def pick(i, lotto):
    l = randint(1, 45)
    for j in range(i):
        if l == lotto[j]:
            return pick(i, lotto)
    return l


#############################################
lotto = []
for i in range(6):
    l = pick(i, lotto)
    lotto.append(l)

print(lotto)
