# 다른PL : 기본형, 객체, ...
# Python : 기본형 없고 다 객체(int, str, ...)


# 객체간의 관계
#   Human has a Dog - 키우는 개
#   Dog has a Human - 주인
######################
class Human:
    def __init__(self, name, age, pet):
        self.name = name
        self.age = age
        self.pet = pet

    def printHumanInfo(self):
        print(self.name, self.age)
        self.pet.printDogInfo()


class Dog:
    def __init__(self, name, species, bug):
        self.name = name
        self.species = species
        self.bug = bug

    def printDogInfo(self):
        print(self.name, self.species)
        self.bug.printBugInfo()


class Bug:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def printBugInfo(self):
        print(self.name, self.size)


###################
# 이름이 벼룩, 크기가 1mm인 벌레
# 출력

b = Bug("벼룩", 1)
b.printBugInfo()
print("--------")

d = Dog("후추", "말티즈", b)
d.printDogInfo()
print("--------")

h = Human("홍길동", 30, d)
h.printHumanInfo()


