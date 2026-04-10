a = [10, 20]
b = [5, 6]
c = a + b  # 붙이기
print(c)
d = a * 3  # 반복해서 붙이기
print(d)
print("-----")
import numpy as np

aa = np.array([10, 20])
bb = np.array([5, 6])
cc = aa + bb  # 모양이 같으면 같은자리에 있는것끼리 계산
print(cc)
dd = aa * 3
print(dd)  # broadcasting : 모양이 다르면 차원수 높은쪽에 맞춰서 계산
print("-----")

name = np.array(["홍길동", "김길동", "박길동"])
kor = np.array([100, 90, 85])
eng = np.array([10, 50, 20])
mat = np.array([40, 60, 55])

sum = kor + eng + mat
avg = sum / 3
print(avg)
over60 = avg > 60  # 평균이 60점 넘나
print(over60)
    
print(name[over60])  # masking : True인 index만
print(name[kor == 100])  # 국어 100점인 학생 이름
# print(name[15 < eng < 60])
# print(name[(eng > 15) and (eng < 60)])
# &&,and는 가다가 걸리면 스킵
# 지금상황에서는 스킵되면?
# 그래서 & 사용해서 끝까지
print(name[(eng > 15) & (eng < 60)])  # 15 < 영어 < 60인 학생 이름
