# http://openapi.seoul.go.kr:8088/(인증키)/xml/CardSubwayPayFree/1/5/201501/

# 날짜, 노선, 역, 내고타, 안내고타, 내고내리, 안내고내리 csv

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

f = open("C:\\Choi\\CSPF.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")
for y in range(2015, 2026):
    for m in range(1, 13):
        t = "%d%02d" % (y, m)
        hc.request(
            "GET",
            "/575a4655496b636839386f58586542/xml/CardSubwayPayFree/1/999/" + t,
        )

        resBody = hc.getresponse().read()

        ddData = fromstring(resBody)
        rows = ddData.iter("row")
        for r in rows:
            f.write(r.find("USE_MM").text + ",")
            f.write(r.find("SBWY_ROUT_LN_NM").text + ",")
            f.write(r.find("STTN").text + ",")
            f.write(r.find("RMIO_GTON_NOPE").text + ",")
            f.write(r.find("FREECHRG_GTON_NOPE").text + ",")
            f.write(r.find("RMIO_GTOFF_NOPE").text + ",")
            f.write(r.find("FREECHRG_GTOFF_NOPE").text + "\n")
        print(t)

f.close()
hc.close()
