import numpy as np

a = np.random.rand(2, 3)
print(a)
print("-----")

b = np.ceil(a)
print(b)
print("-----")

c = np.floor(a)
print(c)
print("-----")

d = np.rint(a)  # 반올림
print(d)
print("-----")

e = np.round(a, 3)  # 자리수 지정 반올림
print(e)
print("-----")

# 소수점 이하 두번째 자리에서 올림
f = np.ceil(a * 10) / 10
print(f)
print("-----")
# 후속기술들이 표현못하는
g = np.array([1, np.nan, 2, np.inf, 3])
print(g)
print(np.isnan(g))
print(np.isinf(g))
print("-----")

h = np.random.randint(-5, 6, [2, 3])
print(h)
print("-----")

i = np.abs(h)
print(i)

j = np.sqrt(h)
print(j)
