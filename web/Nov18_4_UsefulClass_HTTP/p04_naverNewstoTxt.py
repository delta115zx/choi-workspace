

from pymongo import MongoClient


con = MongoClient("195.168.9.70")
db = con.Choi

f = open("C:/Choi/naverNews.txt", "a", encoding="utf-8")

news = db.naverNews.find()
for n in news:
    f.write("%s\n" % n["txt"])

f.close()
con.close()