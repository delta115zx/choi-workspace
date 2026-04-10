from http.client import HTTPConnection
from json import loads
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

hc = HTTPConnection("openapi.seoul.go.kr:8088")

hc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")

res = hc.getresponse()
resBody = res.read()

hc.close()

dustData = loads(resBody)  # JSON -> python컬렉션
df = pd.DataFrame(dustData["RealtimeCityAir"]["row"])
print(df)

# sns.histplot(df, x="PM") # 히스토그램
# sns.pairplot(df) # 히스토그램 + scatter
# sns.violinplot(df, x="PM")
sns.violinplot(df, x="PM", y="SAREA_NM", palette="winter", hue="SAREA_NM")
plt.show()
