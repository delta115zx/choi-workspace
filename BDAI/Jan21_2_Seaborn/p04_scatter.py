import pandas as pd
import seaborn as sns
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

sns.scatterplot(df, x="내고타", y="내고내려", palette="winter", hue="노선", size="안내고타")
plt.show()