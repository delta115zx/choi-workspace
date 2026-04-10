from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/xy.calculate")
def xyCalculate(xxx:int, yyy:int): # reqParam변수명:자료형, ...
    z = xxx + yyy
    html = "<html><head><meta charset=\"utf-8\"><head><body>"
    html += "<h1>%d<h1>" % z
    html += "</body></html>"
    return HTMLResponse(html)

# 파일업로드때 필요한건데, 설치안하면 post방식 reqParam이 안받아져서
#   pip install python-multipart

@app.post("/gugudan.show")
def gugudan(start:int=Form(), end:int=Form()): # reqParam변수명:자료형=Form(), ...
        html = "<html><head><meta charset=\"utf-8\"><head><body>"
        for x in range(start, end+1):
            html += "<table border=\"1\" style=\"float:left\">" 
            html += "<tr><td>%d단<td><tr>" % x
            for i in range(1, 10):
                html += "<tr><td> 2 x %d = %d</td></tr>" % (i, x * i)
            html += "</table>"
        html += "</body></html>"
        return HTMLResponse(html)