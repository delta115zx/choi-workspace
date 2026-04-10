from fastapi import Form, UploadFile
from fastapi.responses import FileResponse, JSONResponse

from Choi.ChoiFileManager import ChoiFileManager


class FileDAO:
    def __init__(self):
        pass

    async def fileUpload(self, photo: UploadFile, title: str = Form()):
        # 경로쓸때 photoManager.py기준x, homeController.py기준
        try:
            photoFileName = await ChoiFileManager.upload(
                "./fileDAO/files/", photo, "uuid"
            )

            h = {
                "Access-Control-Allow-Origin": "http://localhost:5173",
                "Access-Control-Allow-Credentials": "true",
            }
            result = {"title": title, "file": photoFileName}
            return JSONResponse(result, headers=h)

        except Exception as e:
            print(e)

    def fileGet(self, filename):
        return FileResponse("./fileDAO/files/" + filename, filename=filename)
