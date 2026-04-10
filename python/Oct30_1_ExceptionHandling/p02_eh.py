# y에 1 : 5 - 6 - 11 - 12 - 7 
# y에 0 : 5 - 7(ZDE발생) - 8 - 9 - 11 - 12 - 10
class Calculator:
    def calc(x, y):
        try:
            z = x / y
            return z
        except:
            print("나누기 0?")
            return -999
        finally:
            print("어쨌든 계산 끝")

#########################
x = int(input("x : "))
y = int(input("y : "))

z = Calculator.calc(x, y)
print(z)