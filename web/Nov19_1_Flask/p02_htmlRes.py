from unittest import result
from flask import Flask


app = Flask(__name__)

# http://195.168.9.152:8888/html.test
@app.get("/html.test")
def htmlTest():
    html = "<html><head><meta charset=\"utf-8\"><head><body>"
    html += "<marquee>ㅋㅋ</marquee>"
    html += "</body></html>"
    return html

# http://195.168.9.152:8888/xy.calculate
@app.get("/xy.calculate")
def xyCalculate():
    x = 10
    y = 20
    z = x + y
    html = "<html><head><meta charset=\"utf-8\"><head><body>"
    html += "<h1>%d<h1>" % z
    html += "</body></html>"
    return html

# http://195.168.9.152:8888/gugudan.show
@app.get("/gugudan.show")
def gugudan():
        html = "<html><head><meta charset=\"utf-8\"><head><body>"
        for x in range(2, 10):
            html += "<table border=\"1\" style=\"float:left\">" 
            html += "<tr><td>%d단<td><tr>" % x
            for i in range(1, 10):
                html += "<tr><td> 2 x %d = %d</td></tr>" % (i, x * i)
            html += "</table>"
        html += "</body></html>"
        return html



if __name__ == "__main__":
    app.run("0.0.0.0", 8888, True)