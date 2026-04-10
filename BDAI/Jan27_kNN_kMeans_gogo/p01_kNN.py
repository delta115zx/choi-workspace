# kNN(k-Nearest Neighbor) : k-최근접 이웃
#   지도학습
#   분류
#   가장 가까운 Top k개 뽑아서, 다수결로 결론

# 2차원 -> 피타고라스정리...
# 차원이 높아지면 거리 뭘로 구하나 -> 유클리드 거리
# kNN자체가 유클리드거리고 구하는 알고리즘

# 비행기 : 몇만단위, 게임: 최대100, 아이스크림 : 최대2?
# 저대로 kNN하면 비행기만 크게 영향 끼칠 뿐 -> 동등하게 하려면
#       정규화 : 상수값 -> 비율로

fight = [80, 95, 10, 90, 5, 90, 10, 45, 35, 67]
yok = [20, 5, 90, 10, 95, 10, 90, 55, 65, 33]
label = ["액션", "액션", "조폭", "액션", "조폭", "액션", "조폭", "조폭", "조폭", "액션"]

feature = []
for x in fight:
    feature.append([x])

for i, y in enumerate(yok):
    feature[i].append(y)
# print(feature)

k = int(input("k : "))
newX = float(input("싸움 : "))
newY = float(input("욕 : "))
newMovie = [newX, newY]

# a = ((newf[0] - feature[0][0]) * (newf[0] - feature[0][0])) ** 0.5
# b = ((newf[1] - feature[0][1]) * (newf[1] - feature[0][1])) ** 0.5
# print(a)
# print(b)
# distance1 = a + b
# print(distance1)

# c = ((newf[0] - feature[1][0]) * (newf[0] - feature[1][0])) ** 0.5
# d = ((newf[1] - feature[1][1]) * (newf[1] - feature[1][1])) ** 0.5
# print(c)
# print(d)
# distance2 = c + d
# print(distance2)


def calcDistance(feature, newMovie, fN):
    xx = ((newMovie[0] - feature[fN][0]) * (newMovie[0] - feature[fN][0])) ** 0.5
    yy = ((newMovie[1] - feature[fN][1]) * (newMovie[1] - feature[fN][1])) ** 0.5
    return xx + yy


result = []
result2 = {}
for i in range(len(feature)):
    result.append(calcDistance(feature, newMovie, i))
    result2[calcDistance(feature, newMovie, i)] = i
# print(result)
# print(result2)

result.sort()
print(result)

# print(result2[result[0]],result2[result[1]],result2[result[2]])

# for ddd in range(0, k):
#     print(result2[result[ddd]])

# print(label[result2[result[0]]],label[result2[result[1]]],label[result2[result[2]]])

result3 = {}
keys = []
for i in range(k):
    if label[result2[result[i]]] in result3:
        result3[label[result2[result[i]]]] += 1
    else:
        result3[label[result2[result[i]]]] = 1
        keys.append(label[result2[result[i]]])

print(result3)

result4 = []

for i in range(len(keys)):
    result4.append(result3[keys[i]])

result4.sort(reverse=True)

result5 = {}
for k, v in result3.items():
    result5[v] = k

print(result5[result4[0]])

# newf[50, 50]과 [80, 20]의 거리 = 60
