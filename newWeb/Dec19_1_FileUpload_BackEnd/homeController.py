from fastapi import FastAPI, Form, UploadFile

from fileDAO.fileDAO import FileDAO


app = FastAPI()
fDAO = FileDAO()


@app.post("/file.upload")
async def upload(file: UploadFile, title: str = Form()):
    return await fDAO.fileUpload(file, title)


@app.get("/file.get")
def fileGet(filename):
    return fDAO.fileGet(filename)
