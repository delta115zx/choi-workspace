from datetime import datetime
from http.client import HTTPSConnection
from json import loads
from math import ceil
from fastapi.responses import JSONResponse
import jwt

from Choi.choiDBManager import ChoiDBManager


class ForumDAO:
    def __init__(self):
        self.jwtKey = "12341234"
        self.jwtAlgorithm = "HS256"
        self.postPerPage = 3
        self.setAllPostCount()

    def deletePost(self, no):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
        }
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            sql = "DELETE FROM post WHERE post_no='%s'" % no

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                self.allPostCount -= 1
                return JSONResponse({"result": "게시물 삭제 성공"}, headers=h)
            raise
        except Exception as e:
            print(e)
            return JSONResponse({"result": "게시물 삭제 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def deleteReply(self, no):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
        }
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            sql = "DELETE FROM reply WHERE r_no='%s'" % no

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return JSONResponse({"result": "댓글 삭제 성공"}, headers=h)
            raise
        except Exception as e:
            print(e)
            return JSONResponse({"result": "댓글 삭제 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def editPost(self, no, txt):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
        }
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            txt = str(txt)
            txt = txt.replace('"', "").replace("\\n", "\r\n")
            print(txt)

            sql = "UPDATE post SET post_txt = '%s' WHERE post_no= '%s'" % (txt, no)

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return JSONResponse({"result": "게시물 수정 성공"}, headers=h)
            raise
        except Exception as e:
            print(e)
            return JSONResponse({"result": "게시물 수정 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getPost(self, searchTxt, pageNo):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
        }
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            postCount = self.allPostCount
            if searchTxt != "":
                postCount = self.getPostCount(searchTxt)

            pageCount = ceil(postCount / self.postPerPage)

            searchTxt = "%" + searchTxt + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.postPerPage + 1
            end = pageNo * self.postPerPage

            sql = (
                "SELECT * FROM ( SELECT rownum AS rn, post_no, post_writer, post_color, post_txt, post_date, mem_photo FROM( SELECT * FROM post, member WHERE (post_txt LIKE '%s' or post_writer like '%s') AND post_writer = mem_id ORDER BY post_date desc )) WHERE (rn >= %s AND rn <= %s)"
                % (searchTxt, searchTxt, start, end)
            )

            cur.execute(sql)

            posts = []
            for _, no, writer, color, txt, date, photo in cur:
                posts.append(
                    {
                        "no": no,
                        "writer": writer,
                        "color": color,
                        "txt": txt,
                        "date": datetime.strftime(date, "%Y-%m-%d %H:%M:%S"),
                        "photo": photo,
                        "replys": self.getReply(no),
                    }
                )
            return JSONResponse({"pageCount": pageCount, "result": posts}, headers=h)

        except Exception as e:
            print(e)
            return JSONResponse({"result": "조회 실패"}, headers=h)

        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getPostCount(self, search):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            search = "%" + search + "%"

            sql = (
                "SELECT count(*) FROM post WHERE post_txt LIKE '%s' or post_writer like '%s'"
                % (search, search)
            )
            cur.execute(sql)

            for c in cur:
                return c[0]
        except Exception as e:
            print(e)
            return 0
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getReply(self, r_p_no):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            sql = (
                "SELECT r_no, r_writer, r_color, r_txt, r_date FROM reply WHERE r_p_no = '%s' order by r_date asc"
                % r_p_no
            )

            cur.execute(sql)

            replys = []
            for no, writer, color, txt, date in cur:
                replys.append(
                    {
                        "no": no,
                        "r_p_no": r_p_no,
                        "writer": writer,
                        "color": color,
                        "txt": txt,
                        "date": datetime.strftime(date, "%Y-%m-%d %H:%M:%S"),
                    }
                )
            return replys

        except Exception as e:
            print(e)
            return []

        finally:
            ChoiDBManager.closeConCur(con, cur)

    def setAllPostCount(self):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            sql = "SELECT count(*) FROM post"

            cur.execute(sql)

            for c in cur:
                self.allPostCount = c[0]

        except Exception as e:
            print(e)

        finally:
            ChoiDBManager.closeConCur(con, cur)

    def writePost(self, color, txt, member):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
        }
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            txt = str(txt)
            txt = txt.replace('"', "").replace("\\n", "\r\n")
            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)

            sql = (
                "INSERT INTO post VALUES (post_seq.nextval, '%s', '%s', '%s', sysdate)"
                % (
                    member["id"],
                    color,
                    txt,
                )
            )

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                self.allPostCount += 1
                self.writeWeather(color)
                return JSONResponse({"result": "게시물 작성 성공"}, headers=h)
            raise
        except Exception as e:
            print(e)
            return JSONResponse({"result": "게시물 작성 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def writeReply(self, writer, color, txt, r_p_no):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
        }
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            writer = jwt.decode(writer, self.jwtKey, self.jwtAlgorithm)
            sql = (
                "INSERT INTO reply VALUES (reply_seq.nextval, '%s', '%s', '%s', sysdate, '%s')"
                % (writer["id"], color, txt, r_p_no)
            )

            print(sql)

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return JSONResponse({"result": "댓글 작성 성공"}, headers=h)
            raise
        except Exception as e:
            print(e)
            return JSONResponse({"result": "댓글 작성 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def writeWeather(self, color):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            hc = HTTPSConnection("api.openweathermap.org")
            hc.request(
                "GET",
                "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr",
            )
            resBody = hc.getresponse().read()
            hc.close
            weatherData = loads(resBody)

            sql = "INSERT INTO weather_color VALUES ('%s', '%.3f', '%s', '%s')" % (
                weatherData["weather"][0]["description"],
                weatherData["main"]["temp"],
                weatherData["main"]["humidity"],
                color,
            )

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
        except Exception as e:
            print(e)
            pass
        finally:
            ChoiDBManager.closeConCur(con, cur)
