import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from oracledb import connect

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False
# Python 시각화 라이브러리
# Matplotlib
#   np.array대상(pd.DataFrame이 주력인데)
#   하나하나 다 코딩(막대그패트 색깔 다 다르게)
# Seaborn : Matplotlib라이브러리
#   pd.DataFrame대상
#   로우코딩(테마)

# pip install seaborn
########

con = connect("delta115/cjy0115@195.168.9.190:1521/xe")
sql = "select * from seoul_dust"
df = pd.read_sql(sql, con)
con.close()
print(df)

# 테마 확인
print(plt.colormaps)

# sns.lineplot(df)
sns.lineplot(df, x="SD_DATE", y="SD_PM10", palette="winter", hue="SD_DATE")
plt.title("미세먼지")
plt.show()
