# 2025/11/03 10:52에 실행하면
# 2025/11/03 10:52 서울 미세먼지 출력


# 실행하면 실시간 서울 미세먼지를 csv에 저장
# 2025,11,03,10,52,도심권,중구,10,5,좋음

f = open("C:\\Choi\\1103\\SeoulDust.txt", "a", encoding="utf-8")

from datetime import datetime
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


hc = HTTPConnection("openapi.seoul.go.kr:8088")

hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")

res = hc.getresponse()
resBody = res.read()

hc.close()

seoulDustDataa = fromstring(resBody)
rowsss = seoulDustDataa.iter("row")
for r in rowsss:
    now = datetime.today()
    now = datetime.strftime(now, "%Y,%m,%d,%H,%M")
    msrrgn = r.find("MSRRGN_NM").text
    msrste = r.find("MSRSTE_NM").text
    pm10 = r.find("PM10").text
    pm25 = r.find("PM25").text
    idex = r.find("IDEX_NM").text
    data = "%s,%s,%s,%s,%s,%s\n" % (now, msrrgn, msrste, pm10, pm25, idex)
    f.write(data)

f.close()
