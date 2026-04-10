# 연산자 : 전 PL들 공통
#   다른 언어들은 stack영역이 대상
#   Python은 모든 데이터가 다 heap영역
#       -> 연산자 써놓으면 대충 알아들음
name = input("이름 : ")
height = float(input("키 : "))
age = int(input("나이 : "))
print("---------")
print("키는 %.1fcm고, 나이는 %d살" % (height, age))

# 논리연산자 : 결과로 True/False
# 초과  이상    같다    다르다    이하    미만
# >     >=      ==      !=      <=      <

# a는 키가 130넘어야 타
a = height > 130
print(a)

# b는 나이가 10살 미만이어야 타
b = age < 10  # b = 10 > age 변수를 앞에 배치하는 문화
print(b)

# c는 키가 120이하여야 타
c = (height <= 120)
print(c)

# d는 나이가 5살이어야 타
d = (age == 5)
print(d)

# e는 나이가 10살이아니어야 타
e = (age != 10)
print(e)

# f는 나이가 홀수여야 타
f = (age % 2 == 1)
print(f)

# g는 이름이 홍길동이어야 타
g = (name == "홍길동")
print(g)

#           ~고(and)    ~거나(or)   반대(not)   xor
# 다른PL    &&, &       ||, |       !           ^
# Python    and, &      or, |       not         ^
#           스킵, 끝까지

#   and         or
#   A B         A B
#   o o -> o    o o -> o
#   o x -> x    o x -> o
#   x o -> x    x o -> o
#   x x -> x    x x -> x

# h는 키가 100이상이고, 나이가 80이상이어야
# and로 묶을때는 희귀한걸 앞으로
# h = (height >= 100) and (age >= 80)
h = (age >= 80) and (height >= 100)
print(h)

# i는 나이가 90이상이거나, 키가 80이상이면
# or로 묶을때는 일반적인걸 앞으로
# i = (age >= 90) or (height >= 80)
i = (height >= 80) or (age >= 90)
print(i)

# j는 i의 반대
j = not i
print(j)

# XOR(eXclusive OR - 배타적 OR)
#   a b
#   o o -> x
#   o x -> o
#   x o -> x
#   x x -> o

# k는 나이가 100살 이상이든지, 키가 100이상이든지
# 둘중에 하나만
k = (age >= 100) ^ (height >= 100)
print(k)

# ㅣ은 나이가 20살미만이든지, 나이가 80살초과하든지
l = (age < 20) or (age > 80)
print(l)
# m은 10 <= 나이 <= 30
# m = (10 <= age <= 30) Python은 가능
m = (age <= 30) and (age >= 10)
print(m)
# n은 나이가 10살 넘고, 나이가 50살 넘고
n = age > 50
print(n)

# 단항연산 : not
# 2항연산 : 대부분
# 3항연산
#   조건따져서 변수값 넣을때
#   조건식 ? 참일때값 : 거짓일때값
#   -> Python에는 없음

# Python : 쉽자 -> 공부할거리가 적자
#          효율적인 프로그램 개발하자x
#          대체 가능하면 삭제