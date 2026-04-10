from fastapi.responses import JSONResponse


class CalcDAO:
    def __init__(self):
        pass

    def calc(self, x, y):
        h = {"Access-Control-Allow-Origin": "*"}
        result = {"hab": x + y, "cha": x - y, "gob": x * y, "moks": x % y}
        return JSONResponse(result, headers=h)

    def calc3(self, x, y):
        # http://195.168.9.80:5173만 Cross-Domain AJAX가 가능하게
        h = {
            "Access-Control-Allow-Origin": "http://195.168.9.80:5173",
            "Access-Control-Allow-Credentials": "true",
        }
        result = {"hab": x + y, "cha": x - y, "gob": x * y, "moks": x % y}
        return JSONResponse(result, headers=h)
