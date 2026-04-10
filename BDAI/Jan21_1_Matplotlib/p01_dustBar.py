from http.client import HTTPConnection
from json import loads
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

# 실시간 미세먼지
hc = HTTPConnection("openapi.seoul.go.kr:8088")

hc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")

res = hc.getresponse()
resBody = res.read()

hc.close()

dustData = loads(resBody)  # JSON -> python컬렉션
df = pd.DataFrame(dustData["RealtimeCityAir"]["row"])

pm = df["PM"].to_numpy()
fpm = df["FPM"].to_numpy()
gu = df["MSRSTN_NM"].to_numpy()

print(gu)

xData = np.arange(len(gu))

plt.bar(xData, pm, color="red")
plt.bar(xData, fpm, color="blue", bottom=pm)
plt.xticks(xData, gu)
plt.title("구별 미세먼지")
plt.show()
