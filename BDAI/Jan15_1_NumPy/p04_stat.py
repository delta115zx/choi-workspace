import numpy as np

a = np.random.randint(1, 11, [2, 3])
print(a)
print("-----")

b = np.sum(a)
print(b)

c = np.mean(a)
print(c)

d = a - c  # 각 값에서 평균을 뺌(값이랑 평균이랑 얼마나 차이나나)
e = d**2  # 음수랑 양수를 더해버리면...
#                   -> 제곱해서 음수를 없애
#                   -> 절대값취해도 음수를 없애
# 제곱은 오차를 더크게 보여주기위해 ㅇㅇ
f = np.mean(e)  # 그거의 평균
print(f)

g = np.var(a)  # 분산 : 평균에서 얼마나
print(g)

h = np.sqrt(
    g
)  # 분산 구한거 루트(분산 구할때 제곱을 하니까 단위가 달라짐 (길이 -> 넓이))
print(h)

# 예를 들어 단위가 cm인데 제곱했으니까 cm제곱?
# 루트씌우면 다시cm로 단위맞추려고 ㅇㅇ
i = np.std(a)  # 표준편차
print(i)
print("-----")

j = np.max(a)
print(j)
k = np.min(a)
print(k)

l = np.max(a, axis=0)
print(l)
m = np.min(a, axis=1)
print(m)
print("-----")
print(a)

n = np.argmax(a)  # 최대값 인덱스(제일 큰게 몇번째에) - 동률이면 앞에걸로
print(n)
o = np.argmin(a)  # 최소값 인덱스(제일 작은게 몇번째에) - 동률이면 앞에걸로
print(o)
p = np.argmax(a, axis=0)
print(p)
