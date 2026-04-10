from fastapi import FastAPI
from fastapi.responses import JSONResponse

from player.playerDAO import PlayerDAO


app = FastAPI()
pDAO = PlayerDAO()


@app.get("/player.get")
def playerGet(pageNo, search):
    result = pDAO.get(pageNo, search)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)


@app.get("/player.get.ud")
def playerGetUD(no):
    result = pDAO.getUD(no)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)


@app.get("/player.delete")
def playerDelete(no):
    result = pDAO.delete(no)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)


@app.get("/player.update")
def playerUpdate(no, pname, tname):
    result = pDAO.update(no, pname, tname)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)


@app.get("/player.reg")
def playerReg(pname, tname):
    result = pDAO.Reg(pname, tname)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)
