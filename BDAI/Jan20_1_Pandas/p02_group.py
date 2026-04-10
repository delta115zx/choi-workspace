from oracledb import connect
import pandas as pd

df = pd.read_csv(
    "C:/Choi/LNPS.csv", names=["마트", "품명", "가격", "날짜", "종류", "구"]
)

# 가격 오타인거 삭제
# df = df.sort_values(by="가격", ascending=False)
# print(df.head(10))
df = df[df["가격"] < 3000000]
print(df)
print("-----")

# 평균가
print(df["가격"].mean())
print("-----")

# 종류별 평균가
print(df.groupby("종류")["가격"].mean())
print("-----")

# 구 -> 종류별 평균가
print(df.groupby(["구", "종류"])["가격"].mean())

# 미세먼지
df2 = pd.read_csv(
    "C:/Choi/SeoulDust.csv", names=["날짜", "권역", "구", "미세", "초미세", "상태"]
)

# 구별 미세+초미세 평균
df2["합"] = df2["미세"] + df2["초미세"]
print(df2.groupby("구")["합"].mean())

# 권역별 미세+초미세 평균
print(df2.groupby("권역")["합"].mean())

# 권역별 -> 구별 미세+초미세 평균
print(df2.groupby(["권역", "구"])["합"].mean())

con = connect("delta115/cjy0115@195.168.9.190:1521/xe")
sql = "select * from seoul_dust"
d = pd.read_sql(sql, con)
print(d)

sql = "SELECT SD_MSRSTE ,avg(sd_pm10+sd_pm25) FROM seoul_dust GROUP BY SD_MSRSTE"
d = pd.read_sql(sql, con)
print(d)

sql = "SELECT sd_msrrgn ,avg(sd_pm10+sd_pm25) FROM seoul_dust GROUP BY sd_msrrgn"
d = pd.read_sql(sql, con)
print(d)

sql = "SELECT sd_msrrgn, SD_MSRSTE, avg(sd_pm10+sd_pm25) FROM seoul_dust GROUP BY sd_msrrgn, SD_MSRSTE order by sd_msrrgn, SD_MSRSTE"
d = pd.read_sql(sql, con)
print(d)

con.close()