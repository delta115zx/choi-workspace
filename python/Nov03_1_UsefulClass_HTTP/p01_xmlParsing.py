# AI 훈련용 데이터
#   1) 직접
#   2) 인터넷에서
#       csv파일
#       xml/jso
#       ...
##########################
# 포털사이트
# 정부사이트
# SNS

# 미세먼지 -> 공공데이터 더보기
# 서울시 권역별 실시간 대기환경 현황

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


hc = HTTPConnection("openapi.seoul.go.kr:8088")

hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")

res = hc.getresponse()
resBody = res.read()

hc.close()
#############################
# XML(eXtended Markup Language)
#   데이터를 HTML모양으로 표현해놓은
#   DOM(Document Object Model)객체
#       <tagName attribute="value" attribute="value" ...> : startTag
#       text                                              : text
#       </tagName>                                        : endTag
#############################
seoulDustDataa = fromstring(resBody) # xml파싱시작
rowsss = seoulDustDataa.iter("row") # <row></row>들
for r in rowsss:
    print(r.find("MSRRGN_NM").text)     # <MSRRGN_NM></MSRRGN_NM>
    print(r.find("MSRSTE_NM").text)
    print(r.find("PM10").text)
    print(r.find("PM25").text)
    print(r.find("IDEX_NM").text)
    print("--------")