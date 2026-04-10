from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

from clac.calcDAO import CalcDAO


app = FastAPI()
cDAO = CalcDAO()


@app.get("/calculate.do")
def calc(x: int, y: int):
    return cDAO.calc(x, y)


@app.post("/calculate.do2")
def calc(x: int = Form(), y: int = Form()):
    return cDAO.calc(x, y)

@app.post("/calculate.do3")
def calc(x: int = Form(), y: int = Form()):
    return cDAO.calc3(x, y)
