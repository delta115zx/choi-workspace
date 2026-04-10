from http.client import HTTPConnection
from json import loads
import pandas as pd

hc = HTTPConnection("openapi.seoul.go.kr:8088")

hc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")

res = hc.getresponse()
resBody = res.read()

hc.close()

dustData = loads(resBody)  # JSON -> python컬렉션
dustDF = pd.DataFrame(dustData["RealtimeCityAir"]["row"])
print("------")
dustDF["PM_SUM"] = dustDF["PM"] + dustDF["FPM"]
dustDF["PM_AVG"] = dustDF["PM_SUM"] / 2
print(dustDF[["MSRSTN_NM", "PM_AVG"]])
