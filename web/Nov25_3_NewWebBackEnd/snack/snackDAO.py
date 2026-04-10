from math import ceil
from Choi.choiDBManager import ChoiDBManager


class SnackDAO:
    def __init__(self):
        self.snackPerPage = 3

    def get(self):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.188:1521/xe"
            )

            sql = "select * from nov25_snack order by s_name"
            cur.execute(sql)

            snacks = []
            for name, price in cur:
                snacks.append({"s_name": name, "s_price": price})
            return snacks
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def reg(self, nn, pp):
        # DB에 등록시키고
        # 결과는 JSON으로 나오게
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.188:1521/xe"
            )

            sql = "INSERT INTO nov25_snack VALUES('%s', %d)" % (nn, pp)

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"result": nn + "등록성공"}
            return {"result": nn + "등록실패"}
        except Exception as e:
            print(e)
            return {"result": nn + "등록실패"}
        finally:
            ChoiDBManager.closeConCur(con, cur)


    def getSearch(self, page, search):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.188:1521/xe"
            )

            search = "%" + search + "%"
            start = (page - 1) * self.snackPerPage + 1
            end = page * self.snackPerPage

            sql = (
                "SELECT * from ( SELECT rownum AS rn, s_name, s_price from ( SELECT * FROM nov25_snack WHERE s_name LIKE '%s' ORDER BY s_name)) WHERE rn >= %s AND rn <= %s"
            ) % (search, start, end)
            cur.execute(sql)

            print(cur)

            snacks = []
            for _, name, price in cur:
                snacks.append({"No": _, "s_name": name, "s_price": price})
            return snacks
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)