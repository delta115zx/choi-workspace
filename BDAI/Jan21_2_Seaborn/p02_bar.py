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

# sns.barplot(df)
# sns.barplot(df, x="MSRSTN_NM", y="PM", palette="winter", hue="SAREA_NM")

# 통계가 필요하면 알아서 통계내서 그림(권역별 PM평균 + 검은선은 신뢰구간 95%)
# sns.barplot(df, x="SAREA_NM", y="PM", palette="winter", hue="SAREA_NM")

# 검은선을 표준편차로
# sns.barplot(df, x="SAREA_NM", y="PM", palette="winter", hue="SAREA_NM", errorbar="sd")

# 권역별 데이터 몇개씩
sns.countplot(df, x="SAREA_NM", palette="flare", hue="SAREA_NM")
plt.show()
