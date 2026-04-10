from http.client import HTTPConnection
from json import loads


yy = 2015
f = open("C:/Choi/bus%d.csv" % yy, "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")
 
#for yy in range(2015, 2025):
for mm in range(1, 13):
    for dd in range(1, 32):
        for start in range(1, 41002, 1000):
            t = "%d/%d/%d%02d%02d" % (start, start + 999, yy, mm, dd)
            hc.request(
                "GET",
                "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/" + t,
            )
            resBody = hc.getresponse().read()
 
            busData = loads(resBody)
            if "CardBusStatisticsServiceNew" in busData:
                cbssn = busData["CardBusStatisticsServiceNew"]
                stations = cbssn["row"]
                for s in stations:
                    uy = s["USE_YMD"]
                    y = uy[0:4]
                    m = uy[4:6]
                    d = uy[6:8]
                    rn = s["RTE_NM"].replace(",", ".")
                    ssn = s["SBWY_STNS_NM"].replace(",", ".")
                    gont = s["GTON_TNOPE"]
                    gofft = s["GTOFF_TNOPE"]
                    data = "%s,%s,%s,%s,%s,%.0f,%.0f\n" % (y, m, d, rn, ssn, gont, gofft)
                    f.write(data)
                print(t)
hc.close()
f.close()