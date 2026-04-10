from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/product.reg")
def productReg(name: str, price: int):
    html = '<html><head><meta charset="utf-8"></head><body>'
    html += "<h1>품명 : %s<h1>" % name
    html += "<h1>가격 : %d<h1>" % price
    html += "</body></html>"
    return HTMLResponse(html)
