# 4
from p03_oopModule import Mouse


class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def printInfo(self):
        print(self.title, self.price)


############################
# 객체
m = Mouse("로지텍123", 10000)
m.printInfo()
