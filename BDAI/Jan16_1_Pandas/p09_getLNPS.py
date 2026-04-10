# 서울열린데이터광장
# 생필품 검색
# 서울시 생필품 농수축산물 가격 정보
# Open API
# .csv로
# M_NAME, A_NAME, A_PRICE, P_DATE, M_TYPE_NAME, M_GU_NAME

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


def check(data):
    if data == None:
        return "?"
    return data.strip().replace(",", " ")


f = open("C:\\Choi\\LNPS.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")
for start in range(1, 760002, 1000):
    try:
        t = "%d/%d" % (start, start + 999)
        hc.request(
            "GET",
            "/575a4655496b636839386f58586542/xml/ListNecessariesPricesService/" + t,
        )

        resBody = hc.getresponse().read()

        lnpsData = fromstring(resBody)
        rows = lnpsData.iter("row")
        for r in rows:
            f.write(check(r.find("M_NAME").text) + ",")
            f.write(check(r.find("A_NAME").text) + ",")
            f.write(check(r.find("A_PRICE").text) + ",")
            f.write(check(r.find("P_DATE").text) + ",")
            f.write(check(r.find("M_TYPE_NAME").text) + ",")
            f.write(check(r.find("M_GU_NAME").text) + "\n")
        print(t)
    except:
        pass


hc.close()
f.close()
