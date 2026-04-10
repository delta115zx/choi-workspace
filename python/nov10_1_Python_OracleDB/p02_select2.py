# 과자 평균가

from oracledb import connect


con = connect("delta115/cjy0115@195.168.9.57:1521/xe")

sql = "SELECT avg(s_price) FROM nov07_snack"

cur = con.cursor()

cur.execute(sql)

for result in cur:
    print(result)

cur.close()
con.close()