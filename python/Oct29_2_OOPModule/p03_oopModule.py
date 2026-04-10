# 3
from p04_oopModule import Book


# class
class Mouse:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printInfo(self):
        print(self.name, self.price)


####################################
b = Book("점프투파이썬", 30000)
b.printInfo()
