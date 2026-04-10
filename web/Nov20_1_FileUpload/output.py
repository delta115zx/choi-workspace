from uuid import uuid4
from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import FileResponse, HTMLResponse

from Choi.ChoiFileManager import ChoiFileManager


app = FastAPI()

# 전기신호로 온 값, 알아서 원상복귀(디코딩)

# 파일 업로드
# 1) 인코딩 방식이 바뀌어서 오니
#   pip install python-multipart
# 2) 파일이 업로드 될 폴더 확보(서버)
#   당장 서버를 쓸 수 없는 상황이라면
#   작업끝난 프로젝트 통째로 서버로 보낼테니
#   -> 프로젝트내에 폴더 만들면 + 상대경로
# 3) 요청-응답을 동기식으로
#   파일은 용량이 커, 업로드하는데 시간이 걸림
#   비동기식으로 놔두면 파일이 다 업로드 되지도 않았는데 다음 작업?

# 동기식
#   요청 보내놓고 응답이 올때까지
#   프로그램이 멈춤(응답없음)
# 비동기식 <- fastapi
#   요청 보내놓고 응답이 올때까지
#   프로그램 정상 작동


@app.post("/file.upload")
async def fileUpload(photo: UploadFile, zipp: UploadFile, title: str = Form()):
    photoFolder = "./imggg/"
    photoFileName = await ChoiFileManager.upload(photoFolder, photo, "uuid")

    zipFolder = "./zippp/"
    zipFileName = await ChoiFileManager.upload(zipFolder, zipp, "date")

    html = '<html><head><meta charset="utf-8">'
    html += "</head><body>"
    html += "<h1>%s<h1>" % title
    html += "<h1>%s<h1>" % photoFileName
    html += '<img src="img.get?fName=%s">' % photoFileName
    html += '<a href="zip.get?fName=%s">다운</a>' % zipFileName
    html += "</body></html>"
    return HTMLResponse(html)

@app.get("/zip.get")
def zipGet(fName: str):
    folder = "./zippp/"
    return FileResponse(folder + fName, filename=fName)

# 요청하면 파일을 응답
# ~~~~/img.get?filename=back_123easd.png
@app.get("/img.get")
def imgGet(fName: str):
    folder = "./imggg/"
    return FileResponse(folder + fName, filename=fName)

    # zfolder = "./zippp/"
    # zcontent = await zipp.read()
    # zfilename = zipp.filename
    # ztype = zfilename[-4:]
    # zfilename = zfilename.replace(ztype, "")
    # zfilename = zfilename + "_" + str(uuid4()) + ztype

    # folder = "./imggg/"
    # content = await photo.read()  # 파일내용 다 불러오면
    # filename = photo.filename  # 사용자가 업로드한 파일명(back.png)
    # type = filename[-4:]  # .png
    # filename = filename.replace(type, "")  # back
    # filename = filename + "_" + str(uuid4()) + type  # back_UUID값.png

    # zf = open(zfolder + zfilename, "wb")  # b : binary(파일)
    # zf.write(zcontent)
    # zf.close()

    # f = open(folder + filename, "wb")  # b : binary(파일)
    # f.write(content)
    # f.close()
    
    # 날짜
    # 로그인 아이디
    # DB seq
    # ...






