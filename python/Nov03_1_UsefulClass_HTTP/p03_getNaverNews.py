# https://developers.naver.com/

# 애플리케이션 등록
#   애플리케이션 이름 : 마음대로
#   사용API : 검색
#   비로그인... : WEB설정 -> 웹사이트 주소 아는거 아무거나
# Client ID : 55xZIfWfDlxCn4HhFSYx
# Client Secret : qFJXlykcLJ

# Documents - 서비스API - 검색

# request parameter
#   클라이언트가 서버에게 전달하는 정보
#   주소 뒤에
# request header
#   클라이언트가 서버에게 전달하는 정보
#   내부적으로

# 인터넷 주소 체계
#   프로토콜://서버주소[:포트번호]/폴더/.../파일
#   ?
#   변수명=값&변수명=값&변수명=값...
#   https://openapi.naver.com/v1/search/news.xml?

# 인터넷 주소에 한글,특수문자x
#   ㅋ -> %2A(URL인코딩)

# 실시간 네이버 뉴스를 AI훈련용 데이터로 확보하는 프로그램
# 1) HTTP통신
# 2) 파싱 -> title, description -> 콘솔출력
# 3) 날짜, title, description -> 파일에

# <b></b>처리하는게 네이버뿐만 아니라, 카카오, ...
#   지금 처리 -> 나중에도 필요할듯 -> 회사가서도
#   -> 처리하기 편하게 정리 좀

# library vs framework

########################################
from datetime import datetime
from http.client import HTTPSConnection
from pydoc import text
from urllib.parse import quote
from xml.etree.ElementTree import fromstring

from Choi.ChoiStringCleaner import ChoiStringCleaner



q = "게임"
q = quote(q)  # ㅋ -> %2A

k = {"X-Naver-Client-Id": "55xZIfWfDlxCn4HhFSYx", "X-Naver-Client-Secret": "qFJXlykcLJ"}

hc = HTTPSConnection("openapi.naver.com")

hc.request("GET", "/v1/search/news.xml?query=" + q, headers=k)

res = hc.getresponse()
resBody = res.read()
hc.close

########################################
f = open("C:\\Choi\\1103\\naverNews.txt", "a", encoding="utf-8")
naverNewsData = fromstring(resBody)
itemsss = naverNewsData.iter("item")
for r in itemsss:
    now = datetime.today()
    now = datetime.strftime(now, "%Y\t%m\t%d\t%H\t%M")
    title = ChoiStringCleaner.clean(r.find("title").text)
    description = ChoiStringCleaner.clean(r.find("description").text)
    data = "%s\t%s\t%s\n" % (now, title, description)
    f.write(data)

f.close()
