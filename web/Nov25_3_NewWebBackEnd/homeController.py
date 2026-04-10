from fastapi import FastAPI

from snack.snackDAO import SnackDAO


app = FastAPI()
sDAO = SnackDAO()

# ~~~/snackk.regg?n=빼빼로&p=2000
@app.get("/snackk.regg")
def snackReg(n:str, p:int):
    return sDAO.reg(n, p)

# ~~~/snackk.get
@app.get("/snackk.gett")
def snackGet():
    return sDAO.get()

# ~~~/snack.search?page=2&search=칩
# 칩으로 검색해나온거 2페이지
# 1페이지당 3개씩 나온다치고
@app.get("/snackk.searchh")
def snackSearch(page:int, search:str):
    return sDAO.getSearch(page, search)