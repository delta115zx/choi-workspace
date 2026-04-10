# 숫자 1개 넣으면, 홀수인지 아닌지를 출력해주는 함수
from time import sleep
from tkinter import Y


def printIsOdd(a):
    print(a % 2 == 1)


# 숫자 1개 넣으면, 홀수인지 아닌지 구해주는 함수
def getIsOdd(a):
    odd = a % 2 == 1  # 구했음
    return odd


# 숫자 1개 넣으면, 2배한값 구해주는 함수
def getDouble(a):
    double = a * 2
    return double


# 숫자 4개 리턴불가
# list, set, dict, range, tuple, ... 1개 리턴가능
# 숫자 2개 넣으면, 사칙연산결과를 구해주는 함수
def calculate(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d # Python은 리턴이 여러개 된다x
                      # tuple 1개 리턴시킨건데 () 생략시켰을뿐


##########################
aaa, bbb, _, ddd = calculate(10, 5) # tuple이 나눠서 받는게 가능하니
print(aaa)
print(bbb)
print("-----------")
# 만든 그 함수 써서 13가 홀수인지
printIsOdd(13)
print("-----------")

d = getDouble(5)
sleep(d)  # 프로그램 진행 멈춤

# 그 함수 써서 10이 홀수맞는지 출력
o = getIsOdd(10)
print(o)  # 콘솔창에 출력
