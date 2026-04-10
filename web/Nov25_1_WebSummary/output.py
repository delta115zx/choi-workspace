from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse

from Choi.ChoiFileManager import ChoiFileManager


app = FastAPI()


@app.post("/bmicheck")
async def bmiCheck(
    photo: UploadFile,
    name: str = Form(),
    height: float = Form(),
    weight: float = Form(),
):
    photoFolder = "./img/"
    photoFileName = await ChoiFileManager.upload(photoFolder, photo, "date")

    he = height/100
    bmi = weight / (he * he)

    if bmi >= 39:
            result = "고도비만"
    elif bmi >= 32:
            result = "중도비만"
    elif bmi >= 30:
            result = "경도비만"
    elif bmi >= 24:
            result = "과체중"
    elif bmi >= 10:
            result = "정상"

    html = '<html><head><meta charset="utf-8">'
    html += '<link rel="stylesheet" href="css.get?fName=exam.css">'
    html += "</head><body>"
    html += "<table>"
    html += '<tr><th colspan="2">결과</th></tr>'
    html += (
        '<tr><td colspan="2" align="center"><img src="img.get?fName=%s"></td></tr>'
        % photoFileName
    )
    html += '<tr><td class="iname">이름</td><td class="result">%s</td></tr>' % name
    html += '<tr><td class="iname">키</td><td class="result">%.1f</td></tr>' % height
    html += '<tr><td class="iname">몸무게</td><td class="dd">%.1f</td></tr>' % weight
    html += '<tr><td class="iname">bmi</td><td align="center">%.1f</td></tr>' % bmi
    html += '<tr><td colspan="2" align="center">%s</td></tr>' % result
    html += "</body></html>"
    return HTMLResponse(html)


@app.get("/img.get")
def imgGet(fName: str):
    folder = "./img/"
    return FileResponse(folder + fName, filename=fName)


@app.get("/css.get")
def cssGet(fName: str):
    return FileResponse("./" + fName, filename=fName)
