import numpy as np

a = np.random.randint(1, 11, [2, 3])
b = np.random.randint(1, 11, [2, 3])
print(a)
print(b)
print("-----")
c = a + b  # 연산자를 써서 해도 되는데
print(c)
print("-----")
# 다른 사람이 연산자 말고 메소드형태로 할수도
# d = np.add(a, b)
# d = np.subtract(a, b)
# d = np.multiply(a, b)
# d = np.divide(a, b)
# d = np.mod(a, b) # %
# d = np.power(a, b) # **
d = np.less_equal(a, b)  # <=
print(d)
print("------")

name = np.array(["홍길동", "김길동", "박길동"])
kor = np.array([100, 90, 85])
eng = np.array([10, 50, 20])
mat = np.array([40, 60, 55])
# 평균 60넘는 학생이름
print(name[np.greater(np.divide(np.add(np.add(kor, eng), mat), 3), 60)])
