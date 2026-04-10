from typing import Optional
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

# GET : reqParam이 주소에
#   ...?id=abcd&pw=1234&gender=남&addr=경기
# POST : reqParam이 내부적으로

# checkbox : 변수하나에 값 여러개 -> 주소에 표현불가
#   -> GET방식으로 불가, POST방식이어야
#   reqParam변수명:Optional[list[자료형]]=Form(None)

# textarea : 
#   textarea에서 엔터치면 : \r\n
#   html에서 줄바꿈 : <br>
#       내용을 Python/textarea에서 사용 -> 놔두고
#       내용을 html에서 사용 : \r\n -> <br>

app = FastAPI()

@app.post("/member.sign.up")
def memberSignUp(id:str=Form(),  # reqParam변수명:자료형=Form(기본값)
                 pw:str=Form(), 
                 gender:str=Form(), 
                 addr:str=Form(), 
                 hobby:Optional[list[str]]=Form(None),
                 comment:str=Form()
                 ):
    html = "<html><head><meta charset=\"utf-8\"><head><body>"
    html += "<h1>%s<h1>" % id
    html += "<h1>%s<h1>" % pw
    html += "<h1>%s<h1>" % gender
    html += "<h1>%s<h1>" % addr
    if hobby != None:
        html += "<h1>취미<h1>"
        for h in hobby:
            html += h + " "
        html += "<br>"
    comment = comment.replace("\r\n", "<br>")
    html += "<h1>%s<h1>" % comment
    print(comment)
    html += "</body></html>"
    return HTMLResponse(html)