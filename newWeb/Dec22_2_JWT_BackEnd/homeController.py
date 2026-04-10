from fastapi import FastAPI

from product.productDAO import productDAO


app = FastAPI()
pDAO = productDAO()


@app.get("/product.reg")
def regProduct(name: str, price: int):
    return pDAO.reg(name, price)


@app.get("/product.get")
def getProduct(jwt: str):
    return pDAO.get(jwt)


@app.get("/product.jwt.update")
def productJWTUpdate(jwtt: str):
    return pDAO.update(jwtt)
