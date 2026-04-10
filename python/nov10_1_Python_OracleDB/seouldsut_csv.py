# 2025/11/03 10:52에 실행하면
# 2025/11/03 10:52 서울 미세먼지 출력


# 실행하면 실시간 서울 미세먼지를 csv에 저장
# 2025,11,03,10,52,도심권,중구,10,5,좋음

f = open("C:\\Choi\\SeoulDust.csv", "a", encoding="utf-8")


from oracledb import connect

con = connect("delta115/cjy0115@195.168.9.232:1521/xe")  # 연결


sql = "select * from seoul_dust"  # SQL(;빼고)

cur = con.cursor()  # DB관련작업 총괄 객체 겸 결과

cur.execute(sql)  # 실행

for sd_date, sd_msrrgn, sd_msrste, sd_pm10, sd_pm25, sd_idex in cur:
    data = "%s, %s, %s, %s, %s, %s\n" % (
        sd_date,
        sd_msrrgn,
        sd_msrste,
        sd_pm10,
        sd_pm25,
        sd_idex,
    )
    f.write(data)

cur.close()
con.close()


f.close()
