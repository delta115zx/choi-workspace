from fastapi import FastAPI
from fastapi.responses import JSONResponse

from product.productDAO import ProductDAO
from seller.sellerDAO import SellerDAO


app = FastAPI()
sDAO = SellerDAO()
pDAO = ProductDAO()

@app.get("/seller.get")
def sellerGet(page, search):
    result = sDAO.get(page, search)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)

@app.get("/seller.get.detail")
def sellerGet(no):
    result = sDAO.getDetail(no)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)

@app.get("/seller.delete")
def sellerGet(no):
    result = sDAO.delete(no)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)

@app.get("/seller.update")
def sellerGet(no, name, addr):
    result = sDAO.update(no, name, addr)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)

@app.get("/seller.reg")
def sellerReg(namee, bdd, addrr):
    result = sDAO.reg(namee, bdd, addrr)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)


@app.get("/product.get")
def productGet(page, search):
    result = pDAO.get(page, search)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)

@app.get("/product.detail.get")
def productGet(no):
    result = pDAO.getDetail(no)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)

@app.get("/product.detail.delete")
def productGet(no):
    result = pDAO.delete(no)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)

@app.get("/product.detail.update")
def productGet(no, na, price, stock):
    result = pDAO.update(no, na, price, stock)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)

@app.get("/product.reg")
def productReg(namee, pricee, stockk, p_s_noo):
    result = pDAO.reg(namee, pricee, stockk, p_s_noo)
    h = {"Access-Control-Allow-Origin": "*"}
    return JSONResponse(result, headers=h)
