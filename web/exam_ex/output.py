from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

# 1) CSS파일 안불러짐 = ???
# 2) 사용자가 이상한 값 넣으면

@app.get("/unit.convert")
def unitConvert(num:float, what:str):

    if what == "len":
        result = num * 0.393701
        unit1 = "cm"
        unit2 = "inch"
    elif what == "size":
        result = num * 0.3025
        unit1 = "m²"
        unit2 = "평"
    else:
        result = num * (9/5) + 32
        unit1 = "°C"
        unit2 = "°F"

    html = "<html><head><meta charset=\"utf-8\">"
    html += "<link rel=\"stylesheet\" herf=\"nov194.css\">"
    html += "</head><body>"
    html += "<table>"
    html += "<tr><td>변환결과</td></tr>"
    html += "<tr><td align=\"center\">%.1f %s</td></tr>" % (num, unit1)
    html += "<tr><td align=\"center\">▼</td></tr>"
    html += "<tr><td align=\"center\">%.1f %s</td></tr>" % (result, unit2)
    html += "</table>"
    html += "</body></html>"
    return HTMLResponse(html)