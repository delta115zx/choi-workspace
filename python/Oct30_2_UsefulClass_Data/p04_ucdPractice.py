from datetime import datetime

birthday = input("생년월일(yyyy/mm/dd) : ")
print("--------")

now = datetime.today()
curYear = now.year
birthYear = int(birthday[0:4])
age = curYear - birthYear + 1
print("나이(한국나이) : %d" % age)
birthday2 = datetime.strptime(birthday, "%Y/%m/%d")
yoil = datetime.strftime(birthday2, "%A")
print("요일 : %s" % yoil)
