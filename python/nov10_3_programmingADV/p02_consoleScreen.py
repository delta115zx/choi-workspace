from p02_guest import Guest


class ConsoleScreen:
    def getGuestInfo():
        name = input("이름 : ")
        height = input("키 : ")
        weight = input("몸무게 : ")
        return Guest(name, height, weight)
    
    def printResult(guest):
        print("BMI : %.2f" % guest.bmi) 
        print("%s씨는 %s" % (guest.name, guest.result))