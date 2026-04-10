from calendar import c
from fastapi import FastAPI, Form, UploadFile

from forum.forumDAO import ForumDAO
from member.memberDAO import MemberDAO


app = FastAPI()
mDAO = MemberDAO()
fDAO = ForumDAO()


@app.post("/member.edit")
async def edit(
    photo: UploadFile,
    member: str = Form(),
    pw: str = Form(),
    name: str = Form(),
    postcode: str = Form(),
    address: str = Form(),
    detailAddress: str = Form(),
):
    return await mDAO.edit(photo, member, pw, name, postcode, address, detailAddress)


@app.post("/member.edit.nophoto")
async def editNoPhoto(
    member: str = Form(),
    pw: str = Form(),
    name: str = Form(),
    postcode: str = Form(),
    address: str = Form(),
    detailAddress: str = Form(),
):
    return await mDAO.editNoPhoto(member, pw, name, postcode, address, detailAddress)


@app.post("/sign.up")
async def signUp(
    photo: UploadFile,
    id: str = Form(),
    pw: str = Form(),
    name: str = Form(),
    jumin1: str = Form(),
    jumin2: str = Form(),
    postcode: str = Form(),
    address: str = Form(),
    detailAddress: str = Form(),
):
    return await mDAO.signUp(
        photo, id, pw, name, jumin1, jumin2, postcode, address, detailAddress
    )


@app.get("/id.chk")
def idChk(id: str):
    return mDAO.idChk(id)


@app.get("/member.info.get")
def memberInfoGet(member):
    return mDAO.getMemberInfo(member)


@app.get("/member.info.photo.get")
def memberInfoPhotoGet(file):
    return mDAO.getPhoto(file)


@app.post("/sign.in")
def signIn(id: str = Form(), pw: str = Form()):
    return mDAO.signIn(id, pw)


@app.get("/sign.in.exp.refresh")
def signInExpRefresh(member):
    return mDAO.signInExpRefresh(member)


@app.get("/member.bye")
def memberBye(member, fDAO):
    return mDAO.bye(member, fDAO)


@app.get("/post.write")
def writePost(color: str, txt: str, member):
    return fDAO.writePost(color, txt, member)


@app.get("/post.get")
def getPost(searchTxt, pageNo:int):
    return fDAO.getPost(searchTxt, pageNo)


@app.get("/post.delete")
def deletePost(no):
    return fDAO.deletePost(no)


@app.get("/post.edit")
def editPost(no, txt):
    return fDAO.editPost(no, txt)


@app.get("/reply.write")
def writeReply(writer, color, txt, r_p_no):
    return fDAO.writeReply(writer, color, txt, r_p_no)

@app.get("/reply.delete")
def deleteReply(no):
    return fDAO.deleteReply(no)
