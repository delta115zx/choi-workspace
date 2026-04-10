# 객체간의 관계
#   has a
#   Taxi is a Car : OOP가 말하는 상속


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printInfo(self):
        print(self.name, self.price)


# 우리 쇼핑몰의 모든 상품들은 상품명/가격
# 펜 상품명/가격/색깔

# pen is a Product -> OOP의 상속 사용 가능
#   Product에 있는 멤버들(멤버변수, 메소드)이 Pen쪽으로 상속


# Product로 부터 상속받는 Pen
# Product : 상위/부모/super클래스
# Pen : 하위/자식클래스
class Pen(Product):
    pass


# 우유도 상품이라서, 상품명/가격, 정보출력
# 우유부터 유통기한 -> 기능 확장
#   대부분 PL들은 생성자는 상속 안시켜줌
#   Python은 보통 생성자에서 멤버변수를 결정
#       -> 생성자를 상속 안시켜? -> 멤버변수도 상속 안시켜?
#       => 생성자도 상속됨

# self : 이 클래스
# super : 상위클래스


class Milk(Product):
    # 상속받은게 아니고 새로 만든거 -> 생성자 상속이 의미가 있나...
    # overriding : 상속받아온 생성자 기능 바꾸기 -> overriding이라 부르기는 애매
    # overloading : 똑같은 이름 메소드 여러개 -> overloading이라 부르기도 애매
    def __init__(self, name, price, exp):
        super().__init__(name, price)  # Product에 있는 생성자 부른거 -> 이름, 가격 세팅
        self.exp = exp

    # 정보출력할때 유통기한도 출력하고싶음
    # Product로부터 상속받아온 printInfo는 이름/가격만 출력
    # overriding : 상속받아온 메소드 printInfo의 기능 개조
    # overriding vs overloading
    ##################################
    def printInfo(self):
        super().printInfo()  # Product에 있는 printInfo호출 -> 이름/가격 출력
        print(self.exp)


class Shoes(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def printInfo(self):
        super().printInfo()
        print(self.size)


class Computer(Product):
    def __init__(self, name, price, cpu, ram, ssd):
        super().__init__(name, price)
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    def printInfo(self):
        super().printInfo()
        print(self.cpu, self.ram, self.ssd)

# Product is a object
# Computer is a Product
# LapTop is a Computer
# -> 다단상속
class LapTop(Computer):
    def __init__(self, name, price, cpu, ram, ssd, weight):
        super().__init__(name, price, cpu, ram, ssd)
        self.weight = weight

    def printInfo(self):
        super().printInfo()
        print(self.weight)


p = Pen("모나미153", 500)
p.printInfo()
print("-----------")

m = Milk("서울우유1L", 3000, "20251101")
m.printInfo()
print("-----------")

s = Shoes("조던123", 150000, 270)
s.printInfo()
print("-----------")

c1 = Computer("매직스테이션123", 2000000, "i7-1234", 32, 500)
c1.printInfo()
print("-----------")

c2 = LapTop("그램123", 2500000, "i7-5678", 32, 1000, 3)
c2.printInfo()
