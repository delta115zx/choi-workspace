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

# plt.bar(xData - 0.3, nt, width=0.3, align="edge")
# plt.bar(xData, ant, width=0.3, align="edge")
# plt.bar(xData - 0.3, nn, width=0.3, bottom=nt, align="edge")
# plt.bar(xData, ann, width=0.3, bottom=ant, align="edge")
# plt.xticks(xData, xLabel)
# plt.show()

pieData = [nt.mean(), nn.mean(), ant.mean(), ann.mean()]
pieLabel = ["내고타", "내고내려", "안내고타", "안내고내려"]
plt.pie(
    pieData,
    labels=pieLabel,
    autopct="%.1f%%",
    colors=["red", "orange", "blue", "skyblue"],
)
plt.show()
