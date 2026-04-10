from math import ceil
from Choi.choiDBManager import ChoiDBManager


class PlayerDAO:
    def __init__(self):
        self.playerPerPage = 10
        self.setAllPlayerCount()

    def delete(self, no):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "delete from dec05_player where p_no = %s" % no

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"result": no + "번 선수 삭제 성공"}
            return {"result": no + "번 선수 삭제 실패"}
        except Exception as e:
            print(e)
            return {"result": no + "번 선수 삭제 실패"}
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def get(self, pageNo, search):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            playerCount = self.allPlayerCount
            if search != "":
                playerCount = self.getPlayerCount(search)

            pageCount = ceil(playerCount / self.playerPerPage)

            search = "%" + search + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.playerPerPage + 1
            end = pageNo * self.playerPerPage

            sql = "SELECT * FROM ( SELECT rownum AS rn, p_no, p_name, p_t_name FROM ( SELECT * FROM dec05_player WHERE p_name LIKE '%s' OR p_t_name LIKE '%s' order by p_t_name DESC) ) WHERE rn >= %s AND rn <= %s" % (search, search, start, end)

            cur.execute(sql)

            players = []
            for _, no, pname, tname in cur:
                players.append({"no": no, "pname": pname, "tname": tname})
            result = {"pageCount": pageCount, "players": players}
            return result
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getPlayerCount(self, search):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            search = "%" + search + "%"

            sql = (
                "SELECT count(*) FROM dec05_player WHERE p_name LIKE '%s' OR p_t_name LIKE '%s'"
                % (search, search)
            )
            cur.execute(sql)

            for c in cur:
                return c[0]
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getUD(self, no):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "select * from dec05_player where p_no = %s" % no

            cur.execute(sql)

            for no, pname, tname in cur:
                return {"no": no, "pname": pname, "tname": tname}

        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def Reg(self, pname, tname):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "INSERT INTO DEC05_player VALUES (dec05_seq.nextval, '%s', '%s')" % (
                pname,
                tname,
            )

            cur.execute(sql)

            if cur.rowcount == 1:
                self.allPlayerCount += 1
                con.commit()
                return {"result": pname + "등록 성공"}
            return {"result": pname + "등록 실패"}
        except Exception as e:
            print(e)
            return {"result": pname + "등록 실패"}
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def update(self, no, pname, tname):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = (
                "UPDATE DEC05_PLAYER SET p_name = '%s',  p_t_name = '%s' WHERE P_NO = %s"
                % (pname, tname, no)
            )

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"result": no + "번 선수 수정 성공"}
            return {"result": no + "번 선수 수정 실패"}
        except Exception as e:
            print(e)
            return {"result": no + "번 선수 수정 실패"}
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def setAllPlayerCount(self):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "SELECT count(*) FROM dec05_player order by p_t_name desc"
            cur.execute(sql)

            for c in cur:
                self.allPlayerCount = c[0]
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)
