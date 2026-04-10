import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv(
    "C:/Choi/CSPF.csv",
    names=["날짜", "노선", "역", "내고타", "안내고타", "내고내려", "안내고내려"],
)
df = df.groupby("노선")[["내고타", "안내고타", "내고내려", "안내고내려"]].mean()

nt = df["내고타"].to_numpy()
nn = df["내고내려"].to_numpy()
ant = df["안내고타"].to_numpy()
ann = df["안내고내려"].to_numpy()
xLabel = df.index.to_numpy()

xData = np.arange(len(xLabel))

# 산점도
#   꺾은선그래프인데 선 안이은거 - x
#   분포, x/y관계

# 많이 찍고 타면 많이 찍고 내리는데, 많이 찍는다고 안찍는 사람도 많은건 아니다
plt.scatter(nt, nn, color="green", s=(ant + ann) / 1000)
plt.show()
