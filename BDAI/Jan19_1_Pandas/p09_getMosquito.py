# 2016/5/1 ~ 2026/10/31
# 날짜,물가,집,공원

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


f = open("C:\\Choi\\mosquito.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")
for y in range(2016, 2026):
    for m in range(5, 11):
        for d in range(1, 32):
            t = "%d-%02d-%02d" % (y, m, d)
            hc.request(
                "GET",
                "/575a4655496b636839386f58586542/xml/MosquitoStatus/1/5/" + t,
            )

            resBody = hc.getresponse().read()

            mosData = fromstring(resBody)
            rows = mosData.iter("row")
            for r in rows:
                f.write(r.find("MOSQUITO_DATE").text + ",")
                f.write(r.find("MOSQUITO_VALUE_WATER").text + ",")
                f.write(r.find("MOSQUITO_VALUE_HOUSE").text + ",")
                f.write(r.find("MOSQUITO_VALUE_PARK").text + "\n")
            print(t)

hc.close()
f.close()
