from datetime import datetime
 
f = open("C:/Kwon/subway.csv", "r", encoding="utf-8")
subwaySum = {"Sun": 0, "Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0}
subwayCnt = {"Sun": 0, "Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0}
for line in f.readlines():
    line = line.replace("\n", "").split(",")
    when = "%s,%s,%s" % (line[0], line[1], line[2])
    when = datetime.strptime(when, "%Y,%m,%d")
    yoil = datetime.strftime(when, "%a")
    sum = int(line[5]) + int(line[6])
    subwaySum[yoil] += sum
    subwayCnt[yoil] += 1
f.close()
 
for k, v in subwaySum.items():
    print(k, (v / subwayCnt[k]))
 