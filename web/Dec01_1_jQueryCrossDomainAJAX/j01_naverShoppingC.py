from fastapi import FastAPI, Response

from j01_naverShoppingDAO import NaverShoppingDAO


app = FastAPI()
nsDAO = NaverShoppingDAO()


# http://195.168.9.200:7777/naver.shopping.get?q=가습기
@app.get("/naver.shopping.get")
def nsg(q: str):
    resultt = nsDAO.getNSData(q)
    h = {"Access-Control-Allow-Origin": "*"}
    return Response(resultt, media_type="application/xml", headers=h)
