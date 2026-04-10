from pymongo import ASCENDING, DESCENDING, MongoClient

con = MongoClient("195.168.9.70")
db = con.nov14

# db.JS배열명.find(JS객체).sort({필드명:1, 필드명:-1, ...});
result = db.nov14_student.find().sort([("s_name", ASCENDING), ("s_age", DESCENDING)]);

for s in result:
    print(s["s_name"])
    print(s["s_age"])
    print("-------")

con.close()