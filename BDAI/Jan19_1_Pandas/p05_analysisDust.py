# 미세먼지

# 미세+초미세 구해서
# 평균
# 최소값
# 가장 심했던 구 이름
from oracledb import Cursor, connect
import pandas as pd


# con = connect("delta115/cjy0115@195.168.9.190:1521/xe")
# sql = "select * from seoul_dust"
# d = pd.read_sql(sql, con)
# con.close()
# print(d)
# print("-----")
# d["PM_SUM"] = d["SD_PM10"] + d["SD_PM25"]
# print(d)
# print("-----")
# print(d["PM_SUM"] / 2)
# print("-----")
# print(d["PM_SUM"].min())
# print("-----")
# print(d[d["PM_SUM"] == d["PM_SUM"].max()][["SD_MSRSTE"]])

con = connect("delta115/cjy0115@195.168.9.190:1521/xe")
sql = "select avg(sd_pm10 + sd_pm25), min(sd_pm10 + sd_pm25) from seoul_dust"
df = pd.read_sql(sql, con)
print(df)

sql = "select sd_msrste from seoul_dust where sd_pm10 + sd_pm25 = ( select max(sd_pm10 + sd_pm25) from seoul_dust)"
df = pd.read_sql(sql, con)
con.close()
print(df)