from oracledb import Cursor, connect
import pandas as pd

# 첫줄에 제목
a = pd.read_csv("C:/Choi/titanic.csv")
print(a)
print("------")

# 첫줄에 제목없이 바로 데이터
b = pd.read_csv(
    "C:/Choi/seoulDust.csv", names=["날짜", "권역", "구", "미세", "초미세", "상태"]
)
print(b)
print("------")

# 정형데이터 : OracleDB -> .csv
# 비정형데이터 : MongoDB -> .txt
c = pd.read_csv("C:/Choi/naverBlog.txt", sep="\t", names=["제목", "내용", "광고여부"])
print(c)
print("------")

con = connect("delta115/cjy0115@195.168.9.190:1521/xe")
sql = "select * from seoul_dust"
d = pd.read_sql(sql, con)
print(d)

con.close()
