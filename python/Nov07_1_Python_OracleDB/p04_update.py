# 이름 :
# 수정할 가격 :
# 수정 성공

from oracledb import connect


con = connect("delta115/cjy0115@195.168.9.10:1521/xe")

name = input("이름 : ")
name = "%" + name + "%"
price = int(input("수정할 가격 : "))

sql = "UPDATE nov07_snack " 
sql += "SET s_price = %d " % price
sql += "WHERE s_name like '%s'" % name

cur = con.cursor()
cur.execute(sql)

if cur.rowcount >= 1:
    print("수정 성공")
    con.commit()
else:
    print("수정 실패")

cur.close()
con.close()
