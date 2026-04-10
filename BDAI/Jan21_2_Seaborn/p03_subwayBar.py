from datetime import datetime
from fastapi.background import P
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False
# 버스csv
df = pd.read_csv(
    "C:/Choi/bus2015.csv", names=["년", "월", "일", "버스번호", "정류장", "탄", "내린"]
)

# print(df)
# tavg = df.groupby("버스번호")[["탄"]].mean()
# navg = df.groupby("버스번호")[["내린"]].mean()

df["이용객수"] = df["탄"] + df["내린"]
# print(df["이용객수"])
# avg = df.groupby("버스번호")[["이용객수"]].mean()
# print(avg.index)

# 노선별 이용객수(탄+내린) 평균 막대그래프
# sns.barplot(df, x="버스번호", y="이용객수")
# plt.show()


def test(t):
    date = "%d%02d%02d" % (t["년"], t["월"], t["일"])
    date = datetime.strptime(date, "%Y%m%d")
    return datetime.strftime(date, "%a")

# 요일별 이용객수(탄+내린) 평균 막대그래프
df["요일"] = df.apply(test, axis=1)
# print(df)

sns.barplot(df, x="요일", y="이용객수")
plt.show()
