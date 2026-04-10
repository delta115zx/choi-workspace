import numpy as np

a = np.random.randint(1, 101, [10])
print(a)
print(a[1])
print(a[1:5])
print(a[1:8:2])
print(a[:8:2])
print(a[::2])
print(a[::-1])
print("----------")

b = np.sort(a)  # 오름차순
print(b)
print("---------")

c = np.sort(a)[::-1]  # 내림차순 : 오름차순 + 역순접근
print(c)
print("---------")

d = np.random.randint(1, 101, [3, 5])
print(d)
print("---------")

e = np.sort(d)  # 행별(axis=1이 기본)
print(e)
print("---------")

f = np.sort(d, axis=0)  # 열별
print(f)
print("---------")

# g = 행별 내림차순
# g = np.sort(d)
# for i, v in enumerate(g):
#     g[i] = g[i][::-1]
# print(g)

g = []
for row in d:
    g.append(np.sort(row)[::-1])
g = np.array(g)
print(g)
print("---------")

# h = 열별 내림차순
h = np.sort(d, axis=0)[::-1]
print(h)
