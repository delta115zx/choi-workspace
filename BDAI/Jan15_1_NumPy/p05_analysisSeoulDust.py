# 현실굴복 : DB에 있는거 다 csv로 만들어오고
# numpy

# 서울 실시간 미세먼지

# 구별 미세+초미세 평균

# 제일 심한 구

# 제일 깨끗한 구(동률 다 나오게)

# 평균보다 더러운 구들

import numpy as np

f = open("C:\\Choi\\SeoulDust.csv", "r", encoding="utf8")

dustSum = {}
dustCnt = {}
for line in f.readlines():
    line = line.replace("\n", "").split(",")
    if line[2] in dustSum:
        dustSum[line[2]] += int(line[3]) + int(line[4])
        dustCnt[line[2]] += 1
    else:
        dustSum[line[2]] = int(line[3]) + int(line[4])
        dustCnt[line[2]] = 1
f.close()
name = []
dustAvg = []


for k, v in dustSum.items():
    name.append(k)
    dustAvg.append(v / dustCnt[k])

name = np.array(name)
dustAvg = np.array(dustAvg)

print(name[np.argmax(dustAvg)])

print(name[dustAvg == np.min(dustAvg)])

print(name[dustAvg > np.mean(dustAvg)])