# server : 서비스를 제공하는 컴퓨터
# client : 서비스를 이용하는 컴퓨터
# 컴퓨터 통신
#   socket통신(실시간) : 카톡(내의지와는 상관없이, 상대방이 보내면 그냥 오는)
#       socket서버       - Node.js : 웹소켓서버 구현에 특화
#       socket클라이언트 - JavaScript/React

#   HTTP통신(안실시간) : 인터넷(내가 요청하면 그에대한 응답이 오는)
#       HTTP서버       - Flask/FastAPI
#           웹페이지 요청하면 웹페이지 응답
#           데이터 요청하면 데이터 응답
#           AI가 예측해낸 결과를 누군가가 요청하면 응답
#       HTTP클라이언트 - 
#           데이터 받아와서 AI훈련용데이터로...(Python)
#           AI의 결과 받아서 웹페이지에 띄우자(JavaScript/React)
#########################
# 컴퓨터통신            vs          전화
# protocol(통신방식)                전화, 영통, 카톡영통, ...
# ip주소(23.35.220.251)             전화번호
# DomainName(www.naver.com)         폰에 저장 -> 검색해서 찾
# port번호(서비스 구분하는 번호)    ????

# https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20251030.xml

# HHTP통신
#   protocol : http or https(기본)
#   ip주소 : ???
#   DomainName : www.kma.go.kr
#   port번호 : 기본이면 생략가능
#       http - 80번이 기본
#       https - 443번이 기본
#   /repositary/...
#       폴더명/폴더명/파일명

# Python에서 HTTP통신하는 방법 다양
from http.client import HTTPSConnection


# http or https
hc = HTTPSConnection("www.kma.go.kr") # ip주소(domainName), port번호(폴더명 나오기 전까지)

# HTTP통신 요청(GET방식/POST방식)
hc.request("GET", "/repositary/xml/fct/mon/img/fct_mon1rss_108_20251030.xml")

res = hc.getresponse()  # 응답
resBody = res.read()    # 응답내용
# print(resBody)
print(resBody.decode())# 받아온거 한글처리 해서

hc.close() # 세션 유지시간(기본 30분)이 있어서 자동으로 끊어지기는 하지만

# A랑 B사이에 약속된, B가 사용하기 편하게 데이터 형식이 필요
# 국제 표준 데이터 형식
#   XML : 데이터를 HTML모양으로 표현
#   JSON : 데이터를 JavaScript모양으로 표현
# Python에는 XML/JSON가공하는 기능이 있음

# parsing : 데이터에서 필요없는 부분 날리고 필요한 부분만 추출
# xml parsing
# json parsing