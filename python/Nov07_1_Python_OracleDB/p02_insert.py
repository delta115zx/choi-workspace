from oracledb import connect

# 연결
con = connect("delta115/cjy0115@195.168.9.10:1521/xe")

# 데이터 확보
name = input("이름 : ")
addr = input("주소 : ")
ceo = input("사장이름 : ")
emp = int(input("직원수 : "))

# SQL을 str로(;빼고)
sql = "insert into nov07_company values('%s', '%s', '%s', %d)" % (name, addr, ceo, emp)

# DB관련 작업들 다 총괄해주는 매니저 객체 겸 결과
cur = con.cursor()


# str로 써놓은 SQL을 DB서버로 전송 + 원격실행 + 결과받아오기
cur.execute(sql)

# commit : 실제로 DB서버에 반영
# rollback : 반영시키지말고 취소
# -> DBeaver가 자동commit

# 실행결과
#   CUD : 영향받은 데이터 수
#   R : 데이터
if cur.rowcount == 1:
    print("등록 성공")
    con.commit()
else:
    print("등록 실패")


cur.close()
# 연결해제
con.close()