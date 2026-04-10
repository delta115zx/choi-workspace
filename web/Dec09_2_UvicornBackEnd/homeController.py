from fastapi import FastAPI
from fastapi.responses import JSONResponse

from product.productDAO import ProductDAO


app = FastAPI()
pDAO = ProductDAO()


@app.get("/product.reg")
def productReg(name, price):
    result = pDAO.reg(name, price)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)


@app.get("/product.get")
def productGet(pageNo, search):
    result = pDAO.get(pageNo, search)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)
