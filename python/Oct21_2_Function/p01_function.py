# 영역표시
#   대부분 PL은 {} 사용
#   Python은 : 뒤에 들여쓰기
#       : 뒤에는 무조건 들여쓰기 들어가야

# 컴파일러 방식 : main영역이 존재, 함수는 main영역 밖에 만듬
# 인터프리터 방식 : 따로 main영역이 없음, 함수도 그냥 만들고
#                   함수도 만들고, 호출도하고, 작업도, ...
#                   -> 정리가 안되는 느낌 : 원래 그 맛에 쓰는거

# 함수(function)
#   관련있는 작업들 묶어서 정의해놓고
#   필요할때마다 간편하게 불러다 사용

# 함수명 짓는조건 : 변수명 짓는조건과 같음
#   변수 : 명사형
#   함수 : 동사형

# 1) 함수 정의
#           인자, argument, parameter : 함수 수행하는데 필요한 재료
# def 함수명(변수명, 변수명, ...):
#   내용
#   ...
#   return 값 -> 이 함수의 결과를 호출한쪽으로 돌려줄때
#                어떤 PL든지 return이 여러개 나올수 없음
#                함수 끝

def yaDambae():
    print("어머니한테 가서 돈 받아서")
    print("상가 슈퍼로 가서")
    print("한라산 1갑 달라고 하고")
    print("남은돈 너 과자 하나 사고")
    print("한라산 가져와")
    print("--------------------------")

def test():  # 개발중 -> 내용까지는 모르겠는데
    pass  # 자리만 차지

# parameter부분 다르면(갯수, 자료형) 함수명 똑같이 지어도 됨
#   호출떄 생김새 보면 구별이 되니
# -> 일부러 함수명 똑같게 짓는 테크닉 : overloading
# Python 기본값시스템, parameter지정시스템 
#   -> 호출때 생김새로 구별 불가
#   -> overloading사용불가 -> 모든 함수는 이름이 다 달라야

# 숫자 2개 넣으면 그 합을 출력하는 함수
def printSum(a, b):
    c = a + b
    print(a, b, c)

# 숫자 3개 넣으면 그 합을 출력하는 함수
def printSum2(x, y, z):
    d = x + y + z
    print(x, y, z, d)

# 글자 2개 넣으면 그 글자 붙여서 출력하는 함수
def printStringSum(o, p="ㅠ"):  # p는 따로 값 안넣으면 ㅠ
    i = o + p
    print(i)

################################################
# 2) 정의해놓은 함수호출
# 함수명(값, 값, ...)
yaDambae()
yaDambae()

print("시끄러")

printSum(10, 20)

printSum2(10, 20, 30)
printSum2(20, 40, 60)

printStringSum("ㅋ", "ㅎ")  # o는 ㅋ, p는 ㅎ
printStringSum("ㅋ")  # o는 ㅋ, p는 안넣음 -> p는 기본값
printStringSum(p="ㅋ", o="ㅎ")  # parameter 지정가능
print("-----------")
