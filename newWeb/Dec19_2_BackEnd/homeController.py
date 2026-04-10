from fastapi import FastAPI, Form, UploadFile

from player.playerDAO import PlayerDAO


app = FastAPI()
pDAO = PlayerDAO()


@app.post("/player.reg")
async def regPlayer(photo: UploadFile, name: str = Form(), nickname: str = Form()):
    return await pDAO.reg(photo, name, nickname)


@app.get("/player.get")
def getPlayer(pageNo):
    return pDAO.get(pageNo)


@app.get("/player.delete")
def deletePlayer(name):
    return pDAO.delete(name)


@app.get("/photo.get")
def fileGet(filename):
    return pDAO.photoGet(filename)
