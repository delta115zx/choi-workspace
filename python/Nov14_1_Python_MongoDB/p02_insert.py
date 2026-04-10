from pymongo import MongoClient

# OracleDB
#       table > data
#       SQL로 제어
# MongoDB
#       JS배열 > JS객체 : Python의 list > dict랑 형태가 같음
#       JS로 제어 : Python과 문법이 비슷
#       -> pymongo : MongoDB명령어 거의 그대로 쓰게 해줌
# 연결
con = MongoClient("195.168.9.70")
db = con.nov14

# 데이터 확보
name = input("이름 : ")
age = int(input("나이 : "))

# 명령어 + 서버로 전송 + 원격 실행
result = db.nov14_student.insert_one({"s_name" : name, "s_age" : age});

if result.acknowledged:
    print("동록 성공")

# 연결종료
con.close()