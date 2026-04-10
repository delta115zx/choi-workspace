# 51d1ecd7656d567e9e263d69ff1ebbd4

from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote

from lib.Choi.ChoiStringCleaner import ChoiStringCleaner



hc = HTTPSConnection("dapi.kakao.com")
q = "게임"
q = quote(q)
k = {"Authorization": "KakaoAK 51d1ecd7656d567e9e263d69ff1ebbd4"}

hc.request("GET", "/v2/search/blog?query=" + q, headers=k)
resBody = hc.getresponse().read()
hc.close()

# blogname, title, contents
blogData = loads(resBody)
for b in blogData["documents"]:
    print(ChoiStringCleaner.clean(b["blogname"]))
    print(ChoiStringCleaner.clean(b["title"]))
    print(ChoiStringCleaner.clean(b["contents"]))
