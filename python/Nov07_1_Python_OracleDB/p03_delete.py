from oracledb import connect


con = connect("delta115/cjy0115@195.168.9.10:1521/xe")

name = input("이름 : ")


sql = "delete from nov07_company "
sql += "where c_name = '%s'" % name

cur = con.cursor()
cur.execute(sql)

if cur.rowcount >= 1:
    print("삭제 성공")
    con.commit()
else:
    print("삭제 실패")

cur.close()
con.close()