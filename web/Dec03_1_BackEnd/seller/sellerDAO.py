from datetime import datetime
from math import ceil
from fastapi.background import P
from Choi.choiDBManager import ChoiDBManager


class SellerDAO:
    def __init__(self):
        self.sellerPerPage = 6
        self.setAllSellerCount()

    def delete(self, no):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "delete from dec03_seller where s_no = %d" % int(no)
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return "삭제 성공"
            return "삭제 실패"

        except Exception as e:
            print(e)
            return "삭제 실패"
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getDetail(self, no):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "SELECT * FROM dec03_seller where s_no = %d" % int(no)
            cur.execute(sql)

            for no, name, bd, addr in cur:
                bd = datetime.strftime(bd, "%Y/%m/%d")
                return ({"no": no, "name": name, "bd": bd, "addr": addr})
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getSellerCount(self, search):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            search = "%" + search + "%"

            sql = (
                "SELECT count(*) FROM dec03_seller WHERE s_name LIKE '%s' OR s_addr LIKE '%s'"
                % (search, search)
            )
            cur.execute(sql)

            for c in cur:
                return c[0]
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def get(self, pageNo, search):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sellerCount = self.allSellerCount
            if search != "":
                sellerCount = self.getSellerCount(search)

            pageCount = ceil(sellerCount / self.sellerPerPage)

            search = "%" + search + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.sellerPerPage + 1
            end = pageNo * self.sellerPerPage

            sql = (
                "SELECT * FROM ( SELECT rownum AS rn, s_no, s_name, s_birthday, s_addr FROM ( SELECT * FROM dec03_seller WHERE s_name LIKE '%s' OR s_addr LIKE '%s' order by s_no DESC) ) WHERE rn >= %s AND rn <= %s"
                % (search, search, start, end)
            )
            cur.execute(sql)

            sellers = []
            for _, no, name, bd, addr in cur:
                bd = datetime.strftime(bd, "%Y/%m/%d")
                sellers.append({"no": no, "name": name, "bd": bd, "addr": addr})
            result = {"pageCount": pageCount, "sellers": sellers}
            return result
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def reg(self, n, b, a):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = (
                "insert into dec03_seller values (dec03_seq.nextval, '%s', to_date('%s', 'YYYY-MM-DD'), '%s')"
                % (n, b, a)
            )

            cur.execute(sql)

            if cur.rowcount == 1:
                self.allSellerCount += 1
                con.commit()
                return {"result": n + " 등록 성공"}
            return {"result": n + " 등록 실패"}
        except Exception as e:
            print(e)
            return {"result": n + " 등록 실패"}
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def setAllSellerCount(self):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "SELECT count(*) FROM dec03_seller order by s_no desc"
            cur.execute(sql)

            for c in cur:
                self.allSellerCount = c[0]
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def update(self, no, name, addr):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "update dec03_seller set s_name = '%s', s_addr = '%s' where s_no = %d" % (name, addr, int(no))
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"result": "수정 성공"}
            return {"result": "수정 실패"}

        except Exception as e:
            print(e)
            return {"result": "수정 실패"}
        finally:
            ChoiDBManager.closeConCur(con, cur)