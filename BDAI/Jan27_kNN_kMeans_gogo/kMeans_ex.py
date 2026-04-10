import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame()
df["fight"] = [80, 95, 10, 90, 5]
df["yok"] = [20, 5, 90, 10, 95]

# print(df)
sns.scatterplot(df, x="fight", y="yok")
plt.show()

# kMeans : k개의 평균들
#   군집화
#   k=2로 했다치면
#   1) 데이터들 그래프에 표시
#   2) 랜덤한 점 2개를 그래프에 표시
#   3) 2번에서 찍은 점과 데이터들간의 거리 계산
#   4) 가까운쪽으로 그룹화
#   5) 그룹 내에서 평균내서 그 위치에 점 찍고
#   6) 5번에서 찍은 점과 데이터들간의 거리 계산
#   7) 가까운쪽으로 그룹화
#   5 ~ 7 반복 더이상 그룹 변화가 안 생길때까지 반복

from sklearn.cluster import KMeans

data = df[["fight", "yok"]].to_numpy()

km = KMeans(2)
# print(km.fit_predict(data))
df["group"] = km.fit_predict(data)

sns.scatterplot(df, x="fight", y="yok", palette="rainbow", hue="group")
plt.show()
