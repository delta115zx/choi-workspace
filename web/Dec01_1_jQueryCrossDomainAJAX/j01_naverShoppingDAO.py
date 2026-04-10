from http.client import HTTPSConnection
from urllib.parse import quote

class NaverShoppingDAO:
    def getNSData(self, q):
        q = quote(q)

        k = {"X-Naver-Client-Id": "55xZIfWfDlxCn4HhFSYx", "X-Naver-Client-Secret": "qFJXlykcLJ"}

        hc = HTTPSConnection("openapi.naver.com")

        hc.request("GET", "/v1/search/shop.xml?query=" + q, headers=k)

        resBody = hc.getresponse().read()
        hc.close
        return resBody
