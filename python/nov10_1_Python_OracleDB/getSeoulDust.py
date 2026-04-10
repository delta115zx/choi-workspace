# 2025/11/03 10:52에 실행하면
# 2025/11/03 10:52 서울 미세먼지 출력


# 실행하면 실시간 서울 미세먼지를 csv에 저장
# 2025,11,03,10,52,도심권,중구,10,5,좋음
from oracledb import connect




from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


hc = HTTPConnection("openapi.seoul.go.kr:8088")

hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")

res = hc.getresponse()
resBody = res.read()

hc.close()
##########################
con = connect("delta115/cjy0115@195.168.9.232:1521/xe")

seoulDustDataa = fromstring(resBody)
rowsss = seoulDustDataa.iter("row")
for r in rowsss:
    msrrgn = r.find("SAREA_NM").text
    msrste = r.find("MSRSTN_NM").text
    pm10 = r.find("PM").text
    pm25 = r.find("FPM").text
    idex = r.find("CAI_GRD").text
    
    sql = (
    "INSERT INTO seoul_dust VALUES(sysdate, '%s', '%s', '%s', '%s', '%s')"
    % (msrrgn, msrste, pm10, pm25, idex)
    )
    
    cur = con.cursor() # DB작업 총괄매니저(1회용)
    cur.execute(sql)
    con.commit()
    cur.close()
    
    

con.close()
