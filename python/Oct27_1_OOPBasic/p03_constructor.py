# constructor(생성자) : 객체가 만들어질때 호출되는 메소드
# destructor(소멸자) : 객체가 사라질때 호출되는 메소드

class Phone:
    modelName = None
    phoneNo = None
    price = None

    # default constructor(기본생성자)
    #   생성자 작업을 전혀 하지 않으면
    #   Python이 내부적으로 만들어서 사용
    def __init__(self):  # 생성자
        print("핸드폰 생성")

    def __del__(self): #소멸자
        print("핸드폰 사라짐")

    def showInfo(self):
        print(self.modelName)
        print(self.phoneNo)
        print(self.price)


class Computer:
    cpu = None
    ram = None
    hdd = None

    # 컴이 만들어질떄 뭔가 하고싶어서 -> 생성자
    # 뭐 하게 : 아예 컴 만들면서 cpu/ram/hdd값 넣게
    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def printInfo(self):
        print(self.cpu, self.ram, self.hdd)


class Pen:
    # 여기다 멤버변수 써놓는게 별의미없음(어차피 외부에서 추가가능)
    # -> 잘 안씀
    # name = None
    # color = None
    # price = None
    
    # 다른 PL들이 많이들 활용하는 생성자 overloading이 Python은 불가
    # -> 무조건 생성자는 하나만 존재가능
    # => Python개발자들이 멤버변수를 생성자에서 결정하는 문화
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def printInfo(self):
        print(self.name, self.color, self.price)

class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def printInfo(self):
        print(self.name, self.price)

##########################
# 핸드폰
# 모델명이 갤s23
# 번호가 01058344789
# 가격이47만원
# 정보출력

# 컴퓨터
# cpu가 i7-1234
# ram이 16
# hdd 250
# 정보출력

# 이름이 모나미153, 색깔이 검정, 가격이 500원인 펜
# 정보출력

# 제목이 점프투파이썬, 가격이 20000원인 책
# 정보출력

# 객체 생성
# 변수명 = 클래스명() -> 생성자 호출하는거
myPhone = Phone()
myPhone.modelName = "s23"
myPhone.phoneNo = "01058344789"
myPhone.price = 470000
myPhone.showInfo()
print("-------------")

myCom = Computer("17-1234", 16, 250)
myCom.printInfo()
print("-------------")

myPen = Pen("모나미153", "검정", 500)
myPen.printInfo()
print("-------------")

b = Book("점프투파이썬", 20000)
b.printInfo()