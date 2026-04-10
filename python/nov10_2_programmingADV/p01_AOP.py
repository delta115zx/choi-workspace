# 프로그래밍 패러다임
# PP(Procedural Programming)
#   절차지향프로그래밍
#   순서대로 잘 써서 결과내자
# OOP(Object Oriented Programming)
#   객체지향프로그래밍
#   실생활을 묘사해서, 유지보수하기 좋게 하자
# AOP(Aspect Oriented Programming)
#   관점지향프로그래밍
#   OOP를 다른 관점에서 보자
#   메소드들에 있는 공통된 부분들 따로 정리하자
#################################
class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print(self.name, self.age)

    def ready(self):
        print("씻고 나갈준비")
        print("엘베타고 1층으로")

    # 학교가기, 공원가기, 마트가기의 공통된 부분
    # 나갈준비하기라는 메소드로 따로 정리
    def goToAcademy(self):
        self.ready()
        print("버스타고 학원으로")
    
    def goToMart(self):
        self.ready()
        print("걸어서 마트로")
    
    def goToPark(self):
        self.ready()
        print("앱켜서 자전거하나 빌려서")
        print("공원으로")
    


##############
h1 = human("홍길동", 30)
h1.printInfo()
h1.goToAcademy()
h1.goToMart()
h1.goToPark()
# 학원가기
# 마트가기
# 공원가기