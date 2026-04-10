# Python + OracleDB : cs_Oracle.py -> oracledb.py
# Python + MongoDB : pymongo.py

# 시작 - cmd
#  pip install pymongo
from pymongo import MongoClient


con = MongoClient("195.168.9.70") # 서버주소[:포트번호]
print(con)
db = con.nov14 # con.db명
print(db)
con.close()