# PL 어렵나 -> ㅇㅇ -> 왜?
#   일상언어랑 문법이 너무 다르게 생김
#   PL의 문법이 일상언어랑 비슷하게 되면 쉬워지겠는데

# 효율적인 프로그램 만들자
# 요즘 컴 H/W사양이 좋아져서 -> 효율성이 그닥 안중요
# 알고리즘의 시대 -> 유지보수의 시대
# 좋은 알고리즘 보다는 유지보수하기 좋게 만들자
# 유지보수하기 좋으려면 -> 소스가 알아보기 편해야 -> 일상언어...

# PP(Proedural Programming) : 절차지향프로그래밍
#   함수, 조건문, ... 순서대로 잘 써서 프로그램 만들자

# OOP(Object-Oriented Programming) : 객체지향프로그래밍
#   프로그램소스를 일상언어스럽게 쓰자
#   객체라는걸 써서 리얼월드를 묘사하자
#   객체 : 실생활에 존재하는 어떤 존재(실존안하는 추상적인 개념일수도)
#   객체를 만들려면 클래스가 필요

# function vs method
# f : 기능 모아놓은거
# m : 클래스의 멤버함수 정도로 받아들이면 되겠는데
#       객체의 액션

# 변수
#   전역변수(global variable) : 그냥 밖에 있는거
#       global만 붙이면 어디서든 사용가능
#   지역변수(local variable) : 함수/메소드 속에서 만든거
#       함수/메소드 속에서만 사용가능
#       함수/메소드 진행하는동안만 쓰고 버릴(임시)
#   맴버변수(member variable)
#       member variable, attribute, field
#       객체의 속성

# class : 객체 찍어낼때 쓰는 도장/붕어빵틀
# 다른 PL들 클래스명을 대문자로 시작하는 문화 Python은 딱히
class Dog:
    name = None # member variable : 객체의 속성
    age = None

    def bark(self): # method : 객체의 액션
        print("멍")

    def showDogInfo(self):   # method : 프로그램상 필요한 기능
        print(self.name) # 이 개의 name
        print(self.age)
#################
# object/instance : 찍어낸거/붕어빵
d = Dog()       # 개를 하나만들어서 d라는 변수에 저장
d.name = "후추" # d의 이름이 후추
d.age = 3       # d의 나이가 3살
d.bark()        # d가 짖음
d.showDogInfo()   # d의 정보출력

print("-----------")

d2 = Dog()
d2.name = "만득이"
d2.age = 2
d2.bark()
d2.showDogInfo()
