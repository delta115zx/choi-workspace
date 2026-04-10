import numpy as np

featuree = np.array([[80, 20], [95, 5], [10, 90], [90, 10], [5, 95]])
labell = np.array(["액션", "액션", "조폭", "액션", "조폭"])

from sklearn.neighbors import KNeighborsClassifier

knc = KNeighborsClassifier(3) # k=3(가장 가까운 top3)
knc.fit(featuree, labell) # 학습시키기

fight = float(input("격투씬 : "))
yok = float(input("욕씬 : "))
z = np.array([[fight, yok]])
result = knc.predict(z) # 예측하기
print(result[0])