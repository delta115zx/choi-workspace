from oracledb import connect


class ChoiDBManager:
    @staticmethod
    def makeConCur(info):
        con = connect(info)
        cur = con.cursor()
        return con, cur
    
    @staticmethod
    def closeConCur(con, cur):
        cur.close()
        con.close()