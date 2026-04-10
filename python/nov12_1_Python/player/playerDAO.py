from math import ceil
from Choi.choiDBManager import ChoiDBManager
from player.player2 import Player2
from player.player import Player


class PlayerDAO:
    def __init__(self):
        self.setAllPlayerCount()
        self.playerPerPage = 3

    def delete(self, name):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            sql = "DELETE FROM nov12_player WHERE p_name = '%s'" % (name)

            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return "삭제 성공"
            else:
                return "삭제 실패"
        except Exception as e:
            print(e)
            return "삭제 실패"
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def get(self, pageNo, searchTxt):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            searchTxt = "%" + searchTxt + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.playerPerPage + 1
            end = pageNo * self.playerPerPage

            sql = ("SELECT * from ( SELECT rownum AS rn, p_no, p_name, p_nickname, p_salary, p_position, p_t_name from ( SELECT * FROM nov12_player WHERE p_name LIKE '%s' or p_nickname like '%s' ORDER BY p_t_name)) WHERE rn >= %s AND rn <= %s") % (searchTxt, searchTxt, start, end)
            cur.execute(sql)

            players = []
            for _, no, name, nickname, salary, position, t_name in cur:
                p = Player(no, name, nickname, salary, position, t_name)
                players.append(p)
            return players
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def get2(self, pageNo, searchTxt):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            searchTxt = "%" + searchTxt + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.playerPerPage + 1
            end = pageNo * self.playerPerPage

            sql = "SELECT * FROM ( SELECT rownum AS rn, p_no, p_name, p_nickname, p_salary, p_position, t_name, t_ceo, t_coach FROM ( SELECT p_no, p_name, p_nickname, p_salary, p_position, t_name, t_ceo, t_coach FROM nov12_team, NOV12_PLAYER WHERE t_name = p_t_name  AND (p_name LIKE '%s' OR p_nickname LIKE '%s') ORDER BY t_name, P_POSITION ) ) WHERE rn >= %s AND rn <= %s" % (searchTxt, searchTxt, start, end)
            cur.execute(sql)

            players = []
            for _, no, name, nickname, salary, position, t_name, t_ceo, t_coach in cur:
                p = Player2(no, name, nickname, salary, position, t_name, t_ceo, t_coach)
                players.append(p)
            return players
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getAll(self):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            sql = "SELECT * FROM nov12_player ORDER BY p_t_name, p_position"
            cur.execute(sql)

            players = []
            for no, name, nickname, salary, position, t_name in cur:
                p = Player(no, name, nickname, salary, position, t_name)
                players.append(p)
            return players
        
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getMaxSalary(self):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            sql = "SELECT p_no, p_name, p_nickname, p_salary, p_position, t_name, t_ceo, t_coach FROM NOV12_TEAM, NOV12_PLAYER WHERE p_t_name = t_name AND p_salary = ( SELECT max(P_SALARY) FROM NOV12_PLAYER )"
            cur.execute(sql)

            players = []
            for no, name, nickname, salary, position, t_name, t_ceo, t_coach in cur:
                p = Player2(no, name, nickname, salary, position, t_name, t_ceo, t_coach)
                players.append(p)
            return players
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getPageCount(self, searchTxt):
        if searchTxt == "":
            playerCount = self.allPlayerCount
        else:
            playerCount = self.getPlayerCount(searchTxt)
        return ceil(playerCount / self.playerPerPage)

    def getPlayerCount(self, searchTxt):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            searchTxt = "%" + searchTxt + "%"
            sql = "select count(*) from nov12_player WHERE p_name LIKE '%s' or p_nickname like '%s'" % (searchTxt, searchTxt)
            cur.execute(sql)

            for result in cur:
                return result[0]
        except Exception as e:
            print(e)
            return 0
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def reg(self, player):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            sql = "INSERT INTO nov12_player VALUES(nov12_seq.nextval, '%s', '%s', %s, '%s', '%s')" % (player.name, player.nickname, player.salary, player.position, player.t_name)

            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()

                self.allPlayerCount += 1
                return "동록 성공"
            else:
                return "등록 실패"
        except Exception as e:
            print(e)
            return "등록실패"
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def setAllPlayerCount(self):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            sql = "select count(*) from nov12_player"
            cur.execute(sql)

            for result in cur:
                self.allPlayerCount = (result[0]) # allPlayerCount라는 멤버변수에 세팅
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def update(self, name, what, info):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            if what == "닉네임":
                what = "p_nickname"
            elif what == "연봉":
                what = "p_salary"
            elif what == "포지션":
                what = "p_position"

            sql = "UPDATE nov12_player SET %s = '%s' WHERE p_name = '%s'" % (what, info, name)

            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return "수정 성공"
            else:
                return "수정 실패"
        except Exception as e:
            print(e)
            return "수정 실패"
        finally:
            ChoiDBManager.closeConCur(con, cur)
