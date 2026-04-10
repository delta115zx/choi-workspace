# 1. 분석/훈련용 데이터 구축 (Go)
# subway.csv : 10TB

# 2. 전처리 (Hadoop 서버급 컴 여러대 병렬)

# 3. 분석/AI (NumPy/Pandas)

# 4. 시각화

# 5. 3의 결과를 프로그램에서 쓸수있게 Back-end작업

# 6. front-end
# 역별로 탄사람수, 내린사람수 합 구해서
# 적자보는(내린사람>탄사람)인 역이름

# 1. 분석/훈련용 데이터 구축
# subway.csv
########
# 2. 전처리
f = open("C:\\Choi\\subway.csv", "r", encoding="utf8")
rideSum = {}
alightSum = {}
for line in f.readlines():
    line = line.replace("\n", "").split(",")
    if line[4] in rideSum:
        rideSum[line[4]] += int(line[5])
        alightSum[line[4]] += int(line[6])
    else:
        rideSum[line[4]] = int(line[5])
        alightSum[line[4]] = int(line[6])
f.close()

name = []
ride = []
alight = []
for k, v in rideSum.items():
    name.append(k)
    ride.append(v)
    alight.append(alightSum[k])
########
# 3. 분석
import numpy as np

name = np.array(name)
ride = np.array(ride)
alight = np.array(alight)

print(name[ride < alight])
