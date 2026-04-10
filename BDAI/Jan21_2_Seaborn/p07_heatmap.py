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
    "C:/Choi/subway.csv", names=["년", "월", "일", "노선", "역", "탄", "내린"]
)

df["이용객수"] = df["탄"] + df["내린"]
print(df)

# pivot테이블 : 테이블을 요약해놓은 테이블
# 월별 이용객수를 노선으로 찾게
pt = df.pivot_table(index="노선", columns="월", values="이용객수")
print(pt)

sns.heatmap(pt)
plt.show()