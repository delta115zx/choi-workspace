from math import ceil
from os import remove
from fastapi import UploadFile
from fastapi.responses import FileResponse, JSONResponse
from Choi.ChoiFileManager import ChoiFileManager
from Choi.choiDBManager import ChoiDBManager


class PlayerDAO:
    def __init__(self):
        self.photoDir = "./player/playerPhoto/"
        self.playerPerPage = 5
        self.setAllPlayerCount()

    def delete(self, name):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.137:1521/xe"
            )

            h = {
                "Access-Control-Allow-Origin": "http://localhost:5173",
            }

            # 파일명만 챙겨놓고
            filename = self.getPhotoFileName(name)
            sql = "DELETE FROM DEC19_PLAYER WHERE p_name = '%s'" % name

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                # 챙겨놓은 파일명
                remove(self.photoDir + filename)
                self.allPlayerCount -= 1
                return JSONResponse({"result": "삭제 성공"}, headers=h)
            raise
        except Exception as e:
            print(e)
            return JSONResponse({"result": "삭제 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def get(self, pageNo):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.137:1521/xe"
            )

            h = {
                "Access-Control-Allow-Origin": "http://localhost:5173",
            }

            playerCount = self.allPlayerCount

            pageCount = ceil(playerCount / self.playerPerPage)

            pageNo = int(pageNo)
            start = (pageNo - 1) * self.playerPerPage + 1
            end = pageNo * self.playerPerPage

            sql = (
                "SELECT * FROM ( SELECT rownum AS rn, p_name, P_NICKNAME, P_PHOTO FROM ( SELECT * FROM DEC19_PLAYER ORDER BY P_NAME  )) WHERE rn >= %s AND rn <= %s"
                % (start, end)
            )

            cur.execute(sql)

            player = []
            for _, p_name, p_nickname, p_photo in cur:
                player.append(
                    {
                        "name": p_name,
                        "nickname": p_nickname,
                        "photo": p_photo,
                    }
                )
            result = {"pageCount": pageCount, "player": player}
            return JSONResponse(result, headers=h)
        except Exception as e:
            print(e)
            return JSONResponse("조회 실패", headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getPhotoFileName(self, name):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.137:1521/xe"
            )

            h = {
                "Access-Control-Allow-Origin": "http://localhost:5173",
            }

            sql = "select p_photo from dec19_player where p_name = '%s'" % name

            cur.execute(sql)

            for name in cur:
                return name[0]
        except Exception as e:
            print(e)
            return "없음"
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def photoGet(self, filename):
        return FileResponse(self.photoDir + filename, filename=filename)

    async def reg(self, photo, name, nickname):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
            "Access-Control-Allow-Credentials": "true",
        }
        filename = await ChoiFileManager.upload(
            self.photoDir, photo, "uuid", 10 * 1024 * 1024
        )
        if filename == "fail":
            return JSONResponse(
                {"result": "등록 실패(파일)"}, headers=h
            )  # 파일 업로드 실패로 실패

        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.137:1521/xe"
            )

            sql = "INSERT INTO DEC19_PLAYER VALUES ('%s','%s','%s')" % (
                name,
                nickname,
                filename,
            )
            cur.execute(sql)

            if cur.rowcount == 1:
                self.allPlayerCount += 1
                con.commit()
                return JSONResponse({"result": "등록 성공"}, headers=h)
            # return JSONResponse({"result": "등록 실패"}, headers=h)
            raise  # Exception강제발생
        except Exception as e:
            print(e)
            remove(self.photoDir + filename)
            return JSONResponse({"result": "등록 실패"}, headers=h)  # DB문제로 실패
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def setAllPlayerCount(self):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.137:1521/xe"
            )

            sql = "SELECT count(*) FROM DEC19_player order by p_name"
            cur.execute(sql)

            for c in cur:
                self.allPlayerCount = c[0]
        except Exception as e:
            print(e)

        finally:
            ChoiDBManager.closeConCur(con, cur)

    # def reg(self, name, nickname, pname):
    #     try:
    #         con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.137:1521/xe")

    #         h = {
    #             "Access-Control-Allow-Origin": "http://localhost:5173",
    #             "Access-Control-Allow-Credentials": "true",
    #         }

    #         sql = "INSERT INTO DEC19_PLAYER VALUES ('%s','%s','%s')" % (
    #             name,
    #             nickname,
    #             pname,
    #         )

    #         cur.execute(sql)

    #         if cur.rowcount == 1:
    #             con.commit()
    #             return JSONResponse({"result": "등록 성공"}, headers=h)
    #         return JSONResponse({"result": "등록 실패"}, headers=h)
    #     except Exception as e:
    #         print(e)
    #         return JSONResponse({"result": "등록 실패"}, headers=h)
    #     finally:
    #         ChoiDBManager.closeConCur(con, cur)

    # async def fileUpload(self, photo: UploadFile):
    #     # 경로쓸때 photoManager.py기준x, homeController.py기준
    #     try:
    #         photoFileName = await ChoiFileManager.upload(
    #             "./player/playerPhoto/", photo, "uuid", 10
    #         )

    #         return photoFileName

    #     except Exception as e:
    #         print(e)

    # def fileGet(self, filename):
    #     return FileResponse("./player/playerPhoto/" + filename, filename=filename)
