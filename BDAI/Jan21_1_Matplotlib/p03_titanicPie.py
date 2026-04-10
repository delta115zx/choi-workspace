import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

# 타이타닉
df = pd.read_csv("C:/Choi/titanic.csv")

df = df[df["Survived"] == 0]
df = df["Pclass"].value_counts()

pclassList = []
countList = []
for i, pclass in enumerate(df.index):
    pclassList.append(pclass)
    countList.append(df.iloc[i])

# df = df.groupby(["Pclass", "Survived"])["PassengerId"].count()
# print(df)

# c1 = df[1][0]
# c2 = df[2][0]
# c3 = df[3][0]

# 등급별 죽은사람수 파이차트

# data = [c1, c2, c3]
# label = ["c1", "c2", "c3"]
w = {"width": 0.7, "edgecolor": "black", "linewidth": 3}
plt.pie(countList, labels=pclassList, autopct="%.1f%%", wedgeprops=w)
plt.show()
