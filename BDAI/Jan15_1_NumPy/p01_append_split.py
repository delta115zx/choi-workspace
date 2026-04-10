import numpy as np

a = np.random.randint(1, 101, [3, 5])
b = np.random.randint(1, 101, [3, 5])
print(a)
print(b)
print("-----")
c = a + b  # 쌩list면 붙이는데 np.array는 계산
print(c)
print("-----")
d = np.concatenate([a, b])
print(d)
e = np.append(a, b) # 붙여서 1차원으로
print(e)
print("-----")
# axis=0 : 열방향
# axis=1 : 행방향
f = np.concatenate([a, b], axis=1) # 0이 기본값
print(f)
print("-----")
g = np.array_split(a, 2) # 멋대로 2개로
print(g)
print("-----")
# h = np.split(a, 2) # 2등분(갯수가 맞아떨어져야)
h = np.split(a, 3) # 3등분(갯수가 맞아떨어져야)
print(h)