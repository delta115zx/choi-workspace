from math import ceil
from fastapi.responses import JSONResponse
from Choi.choiDBManager import ChoiDBManager


class MenuDAO:
    def __init__(self):
        self.menuPerPage = 5
        self.setAllMenuCount()

    def delete(self, name):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            h = {"Access-Control-Allow-Origin": "*"}

            sql = "DELETE FROM DEC17_MENU WHERE m_name = '%s'" % name
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return JSONResponse({"result": "삭제 성공"}, headers=h)
            return JSONResponse({"result": "삭제 실패"}, headers=h)

        except Exception as e:
            print(e)
            return JSONResponse({"result": "삭제 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def get(self, pageNo):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            h = {"Access-Control-Allow-Origin": "*"}

            menuCount = self.allMenuCount

            pageCount = ceil(menuCount / self.menuPerPage)

            pageNo = int(pageNo)
            start = (pageNo - 1) * self.menuPerPage + 1
            end = pageNo * self.menuPerPage

            sql = (
                "SELECT * FROM ( SELECT rownum AS rn, M_NAME, M_PRICE, M_DESC FROM ( SELECT * FROM DEC17_MENU ORDER BY M_NAME )) WHERE rn >= %s AND rn <= %s"
                % (start, end)
            )

            cur.execute(sql)

            menus = []
            for _, name, price, desc in cur:
                menus.append({"name": name, "price": price, "desc": desc})
            result = {"pageCount": pageCount, "menus": menus}
            return JSONResponse(result, headers=h)
        except Exception as e:
            print(e)
            return JSONResponse({"result: 조회 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def reg(self, name, price, desc):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            h = {"Access-Control-Allow-Origin": "*"}

            sql = "INSERT INTO DEC17_MENU VALUES('%s', %s, '%s')" % (name, price, desc)
            cur.execute(sql)

            if cur.rowcount == 1:
                self.allMenuCount += 1
                con.commit()
                return JSONResponse({"result": "등록 성공"}, headers=h)
            return JSONResponse({"result": "등록 실패"}, headers=h)
        except Exception as e:
            print(e)
            return JSONResponse({"result": "등록 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def setAllMenuCount(self):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            sql = "SELECT count(*) FROM DEC17_MENU order by m_name"
            cur.execute(sql)

            for c in cur:
                self.allMenuCount = c[0]
        except Exception as e:
            print(e)

        finally:
            ChoiDBManager.closeConCur(con, cur)
