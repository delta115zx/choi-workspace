# HTML : 웹사이트
# ------------디자인 부족

# HTML : 웹사이트 뼈대 : 디자인 언어
# CSS : HTML 디자인 서포트 : 디자인 언어
# JS : HTML 이벤트 서포트 : 프로그래밍 언어
# ------------프로그래밍언어쪽 기능 JS가 하면 되는데, JS를 안쓰려고 했었음 -> 프로그래밍 언어 쪽이 부족

# jQuery, React

# 클라이언트가 웹사이트 요청하면
# HTML + CSS를 만들어서 응답하는
# Python프로그램 : Flask, FastAPI, ...
# ------------작업 불편

# Django
##################################################
# 클래식 웹(Java -> Spring, Python -> Django)
#   back-end(FastAPI) : 7
#       프로그램스러운 작업 다 -> 서버에 부담
#       HTML+CSS+JS만들어서 응답 -> 작업불편
#   front-end(JavaScript) : 3
#       유효성검사
#       약간의 효과
# 신형 웹
#   back-end(FastAPI) : 3
#       DB관련 작업만, 작업 결과를 JS쪽에서 쓸 수 있게(XML/JSON)
#   front-end(JavaScript) : 7
#       프로그램스러운 작업(React) -> 사용자쪽에서, 서버 부담 감소
#       JavaScript는 DB랑 연동x
#       DB관련 작업은 back-end쪽을 통해서(AJAX(XML/JSON))

from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/xmll.testt")
def xmlTest():
    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += "<snacks>"
    xml += "<snack>"
    xml += "<s_name>초코파이</s_name>"
    xml += "<s_price>5000</s_price>"
    xml += "</snack>"
    xml += "<snack>"
    xml += "<s_name>마이쮸</s_name>"
    xml += "<s_price>500</s_price>"
    xml += "</snack>"
    xml += "</snacks>"

    # return Response(xml, media_type="application/xml")

    h = {"Access-Control-Allow-Origin" : "*"}
    return Response(xml, media_type="application/xml", headers=h)


@app.get("/jsonn.testt")
def jsonTest():
    json = [
        {"s_name": "초코파이", "s_price": 5000},
        {"s_name": "마이쮸", "s_price": 500},
    ]
    # XML/JSON을 외부에서도 사용 가능하게 하려면
    # Access-Control-Allow-Origin 응답헤더를 세팅
    h = {"Access-Control-Allow-Origin" : "*"}
    return JSONResponse(json, headers=h)