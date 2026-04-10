import numpy as np
from oracledb import connect
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False
# 미세먼지
con = connect("delta115/cjy0115@195.168.9.190:1521/xe")
sql = "select * from seoul_dust"
df = pd.read_sql(sql, con)
con.close()
print(df)

# pd.DataFrame -> np.array
# t = df.to_numpy()
# print(t)
df = df[df["SD_MSRSTE"] == "종로구"]
df = df.sort_values(by="SD_DATE")
print(df)

pm10 = df["SD_PM10"].to_numpy()
pm25 = df["SD_PM25"].to_numpy()
df["SD_DATE"] = df["SD_DATE"].apply(
    lambda d: "%02d/%02d %02d시" % (d.month, d.day, d.hour)
)
date = df["SD_DATE"].to_numpy()
print(date)


_, sub1Conf = plt.subplots()
p1 = sub1Conf.plot(pm10, "r")
sub1Conf.set_xlabel("시간")
sub1Conf.set_ylabel("미세")

sub2Conf = sub1Conf.twinx()
p2 = sub2Conf.plot(pm25, "b")
sub2Conf.set_ylabel("초미세")

sub1Conf.legend(p1 + p2, ["미세", "초미세"])
plt.title("종로구 미세먼지")
plt.xticks(np.arange(len(date)), date)
plt.show()


# 종로구만
# 날짜에 따른 미세/초미세 변화 꺾은선그래프
# 01/20 15시
