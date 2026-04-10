# https://github.com/gyoogle/tech-interview-for-developer/blob/41a7e91356adae7ee598d5ee3c27438449ce55d8/Interview/README.md

from http.client import HTTPSConnection

from bs4 import BeautifulSoup
from regex import P

from ChoiStringCleaner import ChoiStringCleaner


hc = HTTPSConnection("raw.githubusercontent.com")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

hc.request(
    "GET",
    "/gyoogle/tech-interview-for-developer/master/Interview/README.md",
    headers=headers,
)

resBody = hc.getresponse().read().decode("utf-8")

hc.close()

lines = resBody.split("\n")

for line in lines:
    line = line.strip()
    line = ChoiStringCleaner.clean(line)
    print(line)
