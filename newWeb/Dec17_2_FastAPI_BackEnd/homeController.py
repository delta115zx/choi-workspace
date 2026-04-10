from fastapi import FastAPI
from fastapi.responses import JSONResponse

from menuDAO import MenuDAO


app = FastAPI()
mDAO = MenuDAO()


@app.get("/menu.reg")
def menuReg(name, price, desc):
    return mDAO.reg(name, price, desc)


@app.get("/menu.get")
def menuGet(pageNo):
    return mDAO.get(pageNo)


@app.get("/menu.delete")
def menuDelete(name):
    return mDAO.delete(name)
