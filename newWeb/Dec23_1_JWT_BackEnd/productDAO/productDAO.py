from datetime import datetime, timedelta, timezone

from fastapi.responses import JSONResponse
import jwt


class ProductDAO:
    def __init__(self):
        self.jwtKey = "abcd"
        self.jwtAlgorithm = "HS256"

    def get(self, encodedjwt):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            product = jwt.decode(encodedjwt, self.jwtKey, self.jwtAlgorithm)

        except:
            product = {"name": "없", "price": "음"}
        return JSONResponse(product, headers=h)

    def reg(self, name, price):
        h = {"Access-Control-Allow-Origin": "*"}
        result = {
            "name": name,
            "price": price,
            "exp": datetime.now(timezone.utc) + timedelta(seconds=5),
        }

        token = jwt.encode(result, self.jwtKey, self.jwtAlgorithm)

        return JSONResponse({"token": token}, headers=h)
