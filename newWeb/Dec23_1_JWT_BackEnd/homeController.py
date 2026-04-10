from fastapi import FastAPI

from productDAO.productDAO import ProductDAO


app = FastAPI()
pDAO = ProductDAO()


@app.get("/product.reg")
def reg(name: str, price: int):
    return pDAO.reg(name, price)


@app.get("/product.get")
def get(jwt):
    return pDAO.get(jwt)
