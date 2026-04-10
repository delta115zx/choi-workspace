# DB/객체list/Pandas

# 1) 후속기술들이 NumPy를 써서
# 2) 인공신경망(사실은 행렬계산)
#   행렬이 list -> 쌩list보다는 np.array가 낫고
#   인공신경망 값들은 AI가 찾아낼텐데, 구조는 세워줘야
import numpy as np

a = np.zeros([3, 2], dtype=np.int64)
print(a)

b = np.ones([4, 2])
print(b)

c = np.empty([2, 3])  # 값 신경쓰지말고
print(c)

d = np.arange(3, 10, 2)  # Python의 range같은
print(d)

e = np.random.rand(3, 2)  # 0 ~ 1사이 3x2
print(e)

f = np.random.randn(3, 2)  # 평균0, 표준편차1 3x2 -> 많이들 사용
print(f)

g = np.random.randint(1, 5, [3, 2])  # 1 ~ (5-1) 3x2
print(g)
