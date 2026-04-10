# kMeans : k개의 평균들
#   군집화
#   k=2로 했다치면
#   1) 데이터들 그래프에 표시 (데이터들 묶기)
#   2) 랜덤한 점 2개를 그래프에 표시 (randint*100, randint*100 으로표현?)
#   3) 2번에서 찍은 점과 데이터들간의 거리 계산 (거리계산은 유클리드거리로)
#   4) 가까운쪽으로 그룹화 (k=2니까 리스트2개 만들어서 그룹화? -> a1 > a2 인경우 리스트1에 어펜드, 아닌경우 리스트2에 어펜드)
#   5) 그룹 내에서 평균내서 그 위치에 점 찍고 (x들끼리 y들끼리 더해서 len()으로 나눠서 평균내기?)
#   6) 5번에서 찍은 점과 데이터들간의 거리 계산 (거리계산은 유클리드거리로)
#   7) 가까운쪽으로 그룹화 (k=2니까 리스트2개 만들어서 그룹화? -> a1 > a2 인경우 리스트1에 어펜드, 아닌경우 리스트2에 어펜드)
#   5 ~ 7 반복 더이상 그룹 변화가 안 생길때까지 반복 (조건식으로 리스트1 == 새리스트1, 리스트2 == 새리스트2 같은식으로 와일문?)


from operator import index
from random import randint


# 데이터 묶어서 점으로
def makeFeature(xList, yList):
    feature = []
    for i, x in enumerate(xList):
        feature.append([x])
        feature[i].append(yList[i])
    return feature


# 랜덤한 k개를 그래프에 표시
def makeRandomDot(k):
    rDot = []
    for i in range(k):
        rDot.append([randint(0, 100), randint(0, 100)])
    return rDot


# 찍은점과 데이터들간의 거리계산
def calcDistance(feature, rDot):
    k = len(rDot)
    dis = []
    for k in range(k):
        dis.append([])
        for i in range(len(feature)):
            d1 = ((rDot[k][0] - feature[i][0]) * (rDot[k][0] - feature[i][0])) ** 0.5
            d2 = ((rDot[k][1] - feature[i][1]) * (rDot[k][1] - feature[i][1])) ** 0.5
            dis[k].append(d1 + d2)
    return dis


# 가까운쪽으로 그룹화
def grouping(dis, feature):
    groups = []
    for i in range(len(feature)):
        groups.append([])

    for i in range(len(feature)):
        for k in range(len(dis)):
            groups[i].append(dis[k][i])

    nGroups = []
    for i in range(len(dis)):
        nGroups.append([])

    for i in range(len(feature)):
        for k in range(len(dis)):
            if groups[i].index(min(groups[i])) == k:
                nGroups[k].append(feature[i])

    # for i in range(len(nGroups)):
    #     if nGroups[i] == []:
    #         del nGroups[i]

    return nGroups


# 그룹내에서 평균내서 그 위치에 점찍기
def makeMeanDot(nGroups):
    meanDot = []
    x = 0
    y = 0
    for k in range(len(nGroups)):
        for i in range(len(nGroups[k])):
            x += nGroups[k][i][0]
            y += nGroups[k][i][1]
            if len(nGroups[k]) == 0:
                c = 1
            else:
                c = len(nGroups[k])
        meanDot.append([x / c, y / c])
        x = 0
        y = 0
    return meanDot


fight = [80, 95, 10, 90, 5]
yok = [20, 5, 90, 10, 95]

k = int(input("k : "))

while True:
    feature = makeFeature(fight, yok)
    rDot = makeRandomDot(k)
    # print(rDot)

    dis = calcDistance(feature, rDot)
    # print(dis)

    Groups = grouping(dis, feature)
    # print(nGroups)
    ok = "ㅇㅇ"
    for i in range(k):
        if Groups[i] == []:
            ok = "ㄴㄴ"
    if ok == "ㅇㅇ":
        break

while True:
    meanDot = makeMeanDot(Groups)
    oGroup = Groups
    dis = calcDistance(feature, meanDot)

    nGroup = grouping(dis, feature)

    if oGroup == nGroup:
        break

    print("리그룹")
    Groups = nGroup

    meanDot = makeMeanDot(nGroup)

print(nGroup)
