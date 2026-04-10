from datetime import datetime, timedelta, timezone
from fastapi.responses import JSONResponse
import jwt

# 1) OracleDB서버
# 2) uvicorn + FastAPI Back-end서버
# 3) tomcat + React Front-end서버
# 4) 각 사용자의 웹브라우저

# 사용자1 : 웹브라우저써서 3번서버에 웹페이지 요청해서 웹페이지 받아옴
# 사용자2 : 웹브라우저써서 3번서버에 웹페이지 요청해서 웹페이지 받아옴
# 사용자3 : 웹브라우저써서 3번서버에 웹페이지 요청해서 웹페이지 받아옴

# 데이터를 2번서버에 저장 : 공용데이터
# 사용자마다 개별로 데이터를 저장할 공간이 필요할텐데
#   session : 서버 - 사용자 연결에 저장
#             서버랑 연결 끊으면 데이터 삭제
#             session유지시간(조절가능)동안 아무 작업 안하면 자동으로 연결 끊어짐
#             요청 날리면 유지시간 갱신
#   cookie : 사용자PC에 파일로 저장
#             cookie유지시간
#             서버랑 연결 끊든말든 cookie유지시간동안은 데이터 무조건 보존
#   -> cookie 보안상 문제, session은 서버가 바뀌면 기존 서버와의 연결에 있던 그거?

# JWT(Json Web Token)
#   JSON + 암호화 + 시간제한
#   자동갱신x -> 직접 갱신해야 -> 갱신이 따로 없음(똑같은거 또 만들기)

# 로그인해서 30분동안 작업안하면 끊고

# pip install pyjwt

# 현재시간날짜 : datetime.today()
# 현재시간날짜 : datetime.now()
# 현재시간날짜(표준시간대) : datetime.now(timezone.utc)
# 현재시간날짜(표준시간대)로부터 10초 지나서
#       : datetime.now(timezone.utc) + timedelta(seconds=10)


class productDAO:
    def __init__(self):
        self.jwtKey = "abcd"
        self.jwtAlgorithm = "HS256"

    def get(self, encodedjwt):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            result = jwt.decode(
                encodedjwt, self.jwtKey, self.jwtAlgorithm
            )  # 암호화된 str한덩어리 다시 원래대로
            result = {
                "result": "복호화한거",
                "name": result["name"],
                "price": result["price"],
            }
        except jwt.ExpiredSignatureError:
            result = {"result": "만들기는 했는데, 만료"}
        except jwt.DecodeError:
            result = {"result": "만든적 없음"}
        return JSONResponse(result, headers=h)

    def reg(self, name, price):
        h = {"Access-Control-Allow-Origin": "*"}
        result = {
            "name": name,
            "price": price,
            "exp": datetime.now(timezone.utc) + timedelta(seconds=10),
        }  # exp빼고 마음대로(exp는 시간제한)

        # 암호화해서 str한덩어리로
        jwtResult = jwt.encode(result, self.jwtKey, self.jwtAlgorithm)

        # str한덩어리 주기보다는, JSON형태로 주는게 사용하기 쉬울테니
        jwtResult2 = {"choiJWT": jwtResult}
        return JSONResponse(jwtResult2, headers=h)

    def update(self, encodedJWTT):
        h = {"Access-Control-Allow-Origin": "*"}
        try:
            result = jwt.decode(encodedJWTT, self.jwtKey, self.jwtAlgorithm)
            result = {
                "result": "갱신한거",
                "name": result["name"],
                "price": result["price"],
                "exp": datetime.now(timezone.utc) + timedelta(seconds=10),
            }
            result = jwt.encode(result, self.jwtKey, self.jwtAlgorithm)
            result = {"choiJWT": result}
        except jwt.ExpiredSignatureError:
            result = {"result": "만들기는 했는데, 만료"}
        except jwt.DecodeError:
            result = {"result": "만든적 없음"}
        return JSONResponse(result, headers=h)
