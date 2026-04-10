# from oracledb import connect

from Choi.choiDBManager import ChoiDBManager


class Doctor:
    def calculate(guest):
        con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.57:1521/xe")

        if guest.height > 3:
            guest.height /= 100
        guest.bmi = guest.weight / (guest.height * guest.height)

        if guest.bmi >= 39:
            guest.result = "고도비만"
        elif guest.bmi >= 32:
            guest.result = "중도비만"
        elif guest.bmi >= 30:
            guest.result = "경도비만"
        elif guest.bmi >= 24:
            guest.result = "과체중"
        elif guest.bmi >= 10:
            guest.result = "정상"

        sql = "INSERT INTO nov10_bmi VALUES ('%s', %.2f, %.1f, %.2f, '%s')" % (guest.name, guest.height, guest.weight, guest.bmi, guest.result)
        
        cur.execute(sql)
        con.commit()
        ChoiDBManager.closeConCur(con, cur)
