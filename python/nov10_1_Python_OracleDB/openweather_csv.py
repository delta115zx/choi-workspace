
from oracledb import connect


f = open("C:\\Choi\\OpenWeather.csv", "a", encoding="utf-8")

con = connect("delta115/cjy0115@195.168.9.232:1521/xe")

sql = "select * from openweather"

cur = con.cursor()

cur.execute(sql)

for o_date, o_weather, o_temp, o_humidity in cur:
    data = "%s, %s, %s, %s\n" % (o_date, o_weather, o_temp, o_humidity)
    f.write(data)

cur.close()
con.close()
f.close()