# 데이터를 특정형식으로 표현해야
# HTML모양으로 하자 => XML
# XMV보다 더 괜찮은거 없을까
# JavaScript모양으로 하자 -> JSON

# JSON(JavaScript Object Notation)
#   모든면에서 XML보다 우월
#       -> 요즘 데이터 표현은 대부분 JSON
#       -> 가독성은 XML이 더 나아서 -> 각종설정파일로 XML
#   JS객체
#       {멤버변수명:값, 멤버변수명:값, ...} - Python dict와 같은 문법
#   JS배열
#       [값, 값, ...]                       - Python list와 같은 문법
# https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr

from http.client import HTTPSConnection
from json import loads

from oracledb import connect


hc = HTTPSConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = hc.getresponse().read()
hc.close
##################################
con = connect("delta115/cjy0115@195.168.9.57:1521/xe")

weatherData = loads(resBody) # JSON -> Python컬렉션
description = (weatherData["weather"][0]["description"])
temp = (weatherData["main"]["temp"])
humidity = (weatherData["main"]["humidity"])

sql = ("INSERT INTO openweather VALUES (sysdate, '%s', '%s', '%s')") % (description, temp, humidity)

cur = con.cursor()
cur.execute(sql)
con.commit()

cur.close()
con.close()