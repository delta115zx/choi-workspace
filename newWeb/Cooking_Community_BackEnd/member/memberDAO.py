from datetime import datetime, timedelta, timezone
from os import remove
from fastapi.responses import FileResponse, JSONResponse
import jwt

from Choi.ChoiFileManager import ChoiFileManager
from Choi.choiDBManager import ChoiDBManager


class MemberDAO:
    def __init__(self):
        self.photoDir = "./member/profilePhoto/"
        self.jwtKey = "12341234"
        self.jwtAlgorithm = "HS256"

    def bye(self, member, fDAO):
        h = {"Access-Control-Allow-Origin": "*"}

        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )
            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            sql = "DELETE FROM MEMBER WHERE mem_id = '%s'" % member["id"]
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                remove(self.photoDir + member["photo"])
                fDAO.setAllPostCount()
                return JSONResponse({"result": "탈퇴 성공"}, headers=h)
            raise
        except Exception as e:
            print(e)
            return JSONResponse({"result": "탈퇴 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    async def edit(self, photo, member, pw, name, postcode, address, detailAddress):

        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
            "Access-Control-Allow-Credentials": "true",
        }

        filename = await ChoiFileManager.upload(
            self.photoDir, photo, "date", 20 * 1024 * 1024
        )
        if filename == "fail":
            return JSONResponse({"result": "수정 실패(프사)"}, headers=h)
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            addr = postcode + "㉾" + address + "㉾" + detailAddress

            sql = (
                "UPDATE MEMBER SET mem_pw = '%s', mem_name = '%s', mem_address = '%s', mem_photo = '%s' WHERE mem_id = '%s'"
                % (pw, name, addr, filename, member["id"])
            )
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                remove(self.photoDir + member["photo"])
                newMember = {
                    "id": member["id"],
                    "pw": pw,
                    "name": name,
                    "birthday": member["birthday"],
                    "address": addr,
                    "photo": filename,
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
                }
                newMember = jwt.encode(newMember, self.jwtKey, self.jwtAlgorithm)
                return JSONResponse(
                    {"result": "수정 성공", "member": newMember}, headers=h
                )
            raise
        except Exception as e:
            print(e)
            remove(self.photoDir + filename)
            return JSONResponse({"result": "수정 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    async def editNoPhoto(self, member, pw, name, postcode, address, detailAddress):

        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
            "Access-Control-Allow-Credentials": "true",
        }

        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            addr = postcode + "㉾" + address + "㉾" + detailAddress

            sql = (
                "UPDATE MEMBER SET mem_pw = '%s', mem_name = '%s', mem_address = '%s' WHERE mem_id = '%s'"
                % (pw, name, addr, member["id"])
            )

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                newMember = {
                    "id": member["id"],
                    "pw": pw,
                    "name": name,
                    "birthday": member["birthday"],
                    "address": addr,
                    "photo": member["photo"],
                    "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
                }
                newMember = jwt.encode(newMember, self.jwtKey, self.jwtAlgorithm)
                return JSONResponse(
                    {"result": "수정 성공", "member": newMember}, headers=h
                )
            raise
        except Exception as e:
            print(e)
            return JSONResponse({"result": "수정 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getMemberInfo(self, member):
        h = {"Access-Control-Allow-Origin": "*"}

        try:
            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            member = {
                "id": member["id"],
                "pw": member["pw"],
                "name": member["name"],
                "birthday": member["birthday"],
                "address": member["address"],
                "photo": member["photo"],
            }
            return JSONResponse(
                {"result": "멤버 정보 존재", "member": member}, headers=h
            )
        except jwt.ExpiredSignatureError:
            return JSONResponse({"result": "만료"}, headers=h)
        except jwt.DecodeError:
            return JSONResponse({"result": "정보 없음"}, headers=h)

    def getPhoto(self, file):
        print(file)
        return FileResponse(self.photoDir + file, filename=file)

    def getPhotoFileName(self, id):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            sql = "select mem_photo from member where mem_id = '%s'" % id

            cur.execute(sql)

            for name in cur:
                return name[0]
        except Exception as e:
            print(e)
            return "없음"
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def idChk(self, id):
        h = {"Access-Control-Allow-Origin": "http://localhost:5173"}

        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            sql = "SELECT count(*) FROM MEMBER WHERE mem_id = '%s'" % id

            cur.execute(sql)
            for count in cur:
                if count[0] == 0:
                    return JSONResponse(
                        {"result": "사용가능한 아이디 입니다"}, headers=h
                    )
            return JSONResponse({"result": "중복된 아이디 입니다"}, headers=h)
        except Exception as e:
            print(e)
            return JSONResponse({"result": "조회 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def signIn(self, inputID, inputPW):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
            "Access-Control-Allow-Credentials": "true",
        }
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            sql = "select * from member where mem_id='%s'" % inputID
            cur.execute(sql)
            count = 0
            for id, pw, name, birthday, address, photo in cur:
                count += 1
                if inputPW == pw:
                    member = {
                        "id": id,
                        "pw": pw,
                        "name": name,
                        "birthday": datetime.strftime(birthday, "%Y-%m-%d"),
                        "address": address,
                        "photo": photo,
                        "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
                    }
                    member = jwt.encode(member, self.jwtKey, self.jwtAlgorithm)
                    return JSONResponse(
                        {"result": "로그인 성공", "member": member}, headers=h
                    )
                else:
                    return JSONResponse({"result": "로그인 실패(PW)"}, headers=h)
            if count == 0:
                return JSONResponse({"result": "로그인 실패(미가입 ID)"}, headers=h)
            raise
        except Exception as e:
            print(e)
            return JSONResponse({"result": "로그인 실패(DB)"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def signInExpRefresh(self, member):
        h = {"Access-Control-Allow-Origin": "*"}

        try:
            member = jwt.decode(member, self.jwtKey, self.jwtAlgorithm)
            member = {
                "id": member["id"],
                "pw": member["pw"],
                "name": member["name"],
                "birthday": member["birthday"],
                "address": member["address"],
                "photo": member["photo"],
                "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
            }
            member = jwt.encode(member, self.jwtKey, self.jwtAlgorithm)
            return JSONResponse({"result": "갱신 완료", "member": member}, headers=h)
        except jwt.ExpiredSignatureError:
            return JSONResponse({"result": "만료"}, headers=h)
        except jwt.DecodeError:
            return JSONResponse({"result": "정보 없음"}, headers=h)

    async def signUp(
        self, photo, id, pw, name, jumin1, jumin2, postcode, address, detailAddress
    ):
        h = {
            "Access-Control-Allow-Origin": "http://localhost:5173",
            "Access-Control-Allow-Credentials": "true",
        }

        filename = await ChoiFileManager.upload(
            self.photoDir, photo, "date", 20 * 1024 * 1024
        )
        if filename == "fail":
            return JSONResponse({"result": "가입 실패(프사)"}, headers=h)

        if jumin2 == "1" or jumin2 == "2":
            birthday = "19" + jumin1
        else:
            birthday = "20" + jumin1

        addr = postcode + "㉾" + address + "㉾" + detailAddress

        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.190:1521/xe"
            )

            sql = (
                "INSERT INTO MEMBER VALUES ('%s', '%s', '%s', to_date('%s', 'YYYYMMDD'), '%s', '%s')"
                % (
                    id,
                    pw,
                    name,
                    birthday,
                    addr,
                    filename,
                )
            )

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return JSONResponse({"result": "가입 성공"}, headers=h)
            raise
        except Exception as e:
            print(e)
            remove(self.photoDir + filename)
            return JSONResponse({"result": "가입 실패"}, headers=h)
        finally:
            ChoiDBManager.closeConCur(con, cur)
