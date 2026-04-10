from oracledb import connect

con = connect("delta115/cjy0115@195.168.9.57:1521/xe") # 연결

# 데이터확보

sql = "select * from nov07_company" # SQL(;빼고)

cur = con.cursor() # DB관련작업 총괄 객체 겸 결과

cur.execute(sql) # 실행

# for c in cur:
#     print(c[0])
#     print(c[1])

for name, addr, ceo, emp in cur:
    print(name)
    print(addr)
    print("-------")

cur.close()
con.close()
