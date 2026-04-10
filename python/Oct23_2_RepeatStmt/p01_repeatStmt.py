# 반복문
# 푸쉬업 10번 반복 - 반복횟수
# 푸쉬업 점심시간까지 - 반복조건
# ??? - 컬렉션 차례대로 탐색

# 컬렉션 탐색
# for 변수명 in 컬렉션명:
#   내용
from operator import le


a = [45, 234, 11, 100, 50]
for v in a:
    print(v)
print("-----")

# Python에 반복횟수관련 어쩌고x
# range써서 그 느낌
for w in range(1, 6):
    print(w)
print("------")

# 0
# 1
# 2
# 3
# 4

for e in range(0, 5):
    print(e)
print("------")

for r in range(2, 11, 2):
    print(r)
print("-----")

gob = 1
for i in range(1, 11):
    gob *= i
print(gob)
print("---------")

l = ["ㅋ", "ㅎ", "ㅠ", "ㅡ"]
# len(l) : 내용물 갯수 - 4
# range(len(l)) : 0 ~ 3
#  l[0] : ㅋ
for i in range(len(l)):
    print(l[i])
print("------")
for v in l:  # 단순히 값만
    print(v)
print("------")
for i, v in enumerate(l):  # 인덱스, 값
    print(i)
    print(v)
print("--------")

# dict 탐색 
d = {"색깔": "검정", "가격": 500}
for k, v in d.items():
    print(k)
    print(v)
