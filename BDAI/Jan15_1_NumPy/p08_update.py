import numpy as np

a = np.random.randint(1, 11, [10])
print(a)

# 조건, 값, 대상
a = np.where(a % 2 == 0, 999, a)
print(a)
