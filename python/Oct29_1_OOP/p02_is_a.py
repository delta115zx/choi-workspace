class Avengers:
    def __init__(self, realName, age):
        self.realName = realName
        self.age = age

    def printInfo(self):
        print(self.realName, self.age)

    def attack(self):
        print("공격")


class Human:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def eat(self):
        print("냠")

    def printInfo(self):
        print(self.name, self.address)


# IronMan is a Avengers
# IronMan is a Human
# -> 다중상속
# PL마다 다중상속 지원하냐 마냐 -> 대부분 안됨
# Python은 다중상속 가능
#       다중상속 상황에서 이름이 같으면?
#       -> 먼저 상속받은걸로 -> 다중상속 왜?

class IronMan(Avengers, Human):
    def __init__(self, realName, age, com, address):
        super().__init__(realName, age)
        self.com = com
        self.address = address

    def printInfo(self):
        super().printInfo()
        print(self.com)
        print(self.address)


################################

i = IronMan("토니", 40, "자비스", "서울")
i.attack()
i.eat()
i.printInfo()
