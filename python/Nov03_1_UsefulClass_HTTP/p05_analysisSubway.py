# analysisSubway
# 요일별 이용객수 평균
# -> 무슨요일 이용객수 가장 많

from datetime import datetime

mon = 0
moncount = 0
f = open("C:\\Choi\\1103\\subway.csv", "r", encoding="utf-8")
for line in f.readlines():
    if line.startswith("2015,01,15"):
        break
    line = line.replace("\n", "").split(",")
    yyyy = line[0]
    mm = line[1]
    dd = line[2]
    date = yyyy + mm + dd
    date = datetime.strptime(date, "%Y%m%d")
    yoil = datetime.strftime(date, "%a")
    data = "%s %s %s" % (yoil, line[5], line[6])
    if yoil == "Mon":
        monsum = int(line[5]) + int(line[6])
        mon += monsum
        moncount += 1
print(mon)
print(moncount)
print(mon / moncount)
f.close()
