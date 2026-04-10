# 함수
#   정리차원
#   속도는 느려짐(점프연산)
#   -> recursiveCall : 계산용x
#       계산문제는 반복문으로
#   사용자로부터 개발자가 원하는 값 입력받는 용도
def getEven():
    number = int(input("짝수 : ")) # 사용자로부터 숫자 하나 받음
    if number % 2 == 0: #그게 짝수면
        return number # 받은거를 결과로
    else: # 그게 홀수면
        return getEven()

number = getEven()
print("------------")
print("입력한 숫자는 %d" % number)
