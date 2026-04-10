from math import ceil
from Choi.choiDBManager import ChoiDBManager
from team.team import Team


class TeamDAO:
    def __init__(self):
        self.setAllTeamCount()
        self.teamPerPage = 3

    def delete(self, name):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            sql = "DELETE FROM nov12_team WHERE t_name = '%s'" % (name)

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
            start = (pageNo - 1) * self.teamPerPage + 1
            end = pageNo * self.teamPerPage

            sql = ("SELECT * from ( SELECT rownum AS rn, t_name, t_ceo, t_coach from ( SELECT * FROM nov12_team WHERE t_name LIKE '%s' ORDER BY t_name)) WHERE rn >= %s AND rn <= %s") % (searchTxt, start, end)
            cur.execute(sql)

            teams = []
            for _, name, ceo, coach in cur:
                t = Team(name, ceo, coach)
                teams.append(t)
            return teams
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)


    def getAll(self):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            sql = "SELECT * FROM nov12_team ORDER BY t_name"
            cur.execute(sql)

            teams = []
            for name, ceo, coach in cur:
                t = Team(name, ceo, coach)
                teams.append(t)
            return teams
        
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getPageCount(self, searchTxt):
        if searchTxt == "":
            teamCount = self.allTeamCount
        else:
            teamCount = self.getTeamCount(searchTxt)
        return ceil(teamCount / self.teamPerPage)

    def reg(self, team):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            sql = "INSERT INTO nov12_team VALUES('%s', '%s', '%s')" % (team.name, team.ceo, team.coach)

            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()

                self.allTeamCount += 1
                print(self.allTeamCount)
                return "동록 성공"
            else:
                return "등록 실패"
        except Exception as e:
            print(e)
            return "등록실패"
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getTeamCount(self, searchTxt):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            searchTxt = "%" + searchTxt + "%"
            sql = "select count(*) from nov12_team WHERE t_name LIKE '%s'" % searchTxt
            cur.execute(sql)

            for result in cur:
                return result[0]
        except Exception as e:
            print(e)
            return 0
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def setAllTeamCount(self):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            sql = "select count(*) from nov12_team"
            cur.execute(sql)

            for result in cur:
                self.allTeamCount = (result[0]) # allteamCount라는 멤버변수에 세팅
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def update(self, name, what, info):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            if what == "팀 이름":
                what = "t_name"
            elif what == "ceo":
                what = "t_ceo"
            elif what == "감독":
                what = "t_coach"

            sql = "UPDATE nov12_team SET %s = '%s' WHERE t_name = '%s'" % (what, info, name)

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
