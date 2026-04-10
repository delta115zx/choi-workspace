# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/1/5/20151101/

# 2015,01,01 ~ 2024,12,31
# bus2015.csv
# ...

# 2015,01,01,100번(하계동~용산구청),명륜3가.성대입구,108,171
# ...

from http.client import HTTPConnection
from json import loads

# 1 ~ 1000
# 1001 ~ 2000
# ...
# 41001 ~ 42000

hc = HTTPConnection("openapi.seoul.go.kr:8088")

f = open("C:\\Choi\\1104\\bus2015.csv", "a", encoding="utf-8")
for mm in range(1, 13):
    for dd in range(1, 32):
        for start in range(1, 41002, 1000):
            t = "%d/%d/" % (start, start + 999)
            when = "%04d%02d%02d" % (2015, mm, dd)
            hc.request(
                "GET",
                f"/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/"
                + t
                + when,
            )

            resBody = hc.getresponse().read()
            busData = loads(resBody)
            if "CardBusStatisticsServiceNew" in busData:
                cbssn = busData["CardBusStatisticsServiceNew"]
                stations = cbssn["row"]
                for b in stations:
                    useYMD = b["USE_YMD"]
                    y = useYMD[0:4]
                    m = useYMD[4:6]
                    d = useYMD[6:8]
                    rteNM = b["RTE_NM"].replace(",", ".")
                    sbwySTNSNM = b["SBWY_STNS_NM"].replace(",", ".")
                    gton = b["GTON_TNOPE"]
                    gtoff = b["GTOFF_TNOPE"]
                    data = "%s,%s,%s,%s,%s,%.0f,%.0f\n" % (
                        y,
                        m,
                        d,
                        rteNM,
                        sbwySTNSNM,
                        gton,
                        gtoff,
                    )
                    f.write(data)
            print(when)
hc.close()
f.close()
