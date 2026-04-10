# 연산자(operator)
#   =   대입연산자
#       우항에 있는거 좌항에 넣어라
#       모든 연산자 중 우선순위가 가장 낮음
#  +-*/%     산술연산자

x = int(input("x : "))
y = int(input("y : "))
print("--------")
print("x는 %d, y는 %d" % (x, y))

a = x + y
b = x - y
c = x * y
d = x / y
e = x % y # 나머지
print(a,b,c,d,e)
print("--------")

zz = "ㅋ"
yy = "ㅎ"
xx = zz + yy # str + str -> 붙여줌
print(xx)

# ww = x + zz # int + str -> 불가능(다른 언어들은 붙여주는데)
# print(ww)

vv = zz * x # str * int -> 반복(다른 언어들은 안됨)
print(vv)

uu = x / y # int / int -> 소수점이하까지 계산해서(Python은 자료형을 알아서)
print(uu, type(uu))

tt = x // y # 정수 나누기
print(tt)