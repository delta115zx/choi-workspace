# getSubway
# data.seoul.go.kr
#   지하철 -> 서울시 지하철호선별 역별 승하차 인원 정보
#   Open API
#   http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/5/20151101/

#   2015/01/01 ~ 2024/12/31
#   subway.csv
#   2015,01,01,1호선,시청,53000,23000
#   ...

from datetime import datetime
from http.client import HTTPConnection
from re import U
from xml.etree.ElementTree import fromstring


f = open("C:\\Choi\\1103\\subway.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")
for yyyy in range(2015, 2025):
    for mm in range(1, 13):
        for dd in range(1, 32):
            when = "%d%02d%02d" % (yyyy, mm, dd)
            hc.request(
                "GET",
                "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/630/" + when,
            )
            resBody = hc.getresponse().read()

            subwayData = fromstring(resBody)
            rowsss = subwayData.iter("row")
            for r in rowsss:
                useYMD = r.find("USE_YMD").text
                # useYMD = datetime.strptime(useYMD, "%Y%m%d")
                # useYMD = datetime.strftime(useYMD, "%Y,%m,%d")
                y = useYMD[0:4]
                m = useYMD[4:6]
                d = useYMD[6:8]
                sbwyRout = r.find("SBWY_ROUT_LN_NM").text.replace(",", ".")
                sbwyStns = r.find("SBWY_STNS_NM").text
                gtonTnope = r.find("GTON_TNOPE").text
                gtoffTnope = r.find("GTOFF_TNOPE").text
                data = "%s,%s,%s,%s,%s,%s,%s\n" % (
                    y,
                    m,
                    d,
                    sbwyRout,
                    sbwyStns,
                    gtonTnope,
                    gtoffTnope,
                )
                f.write(data)
            print(when)
hc.close
f.close
