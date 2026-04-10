from p01_company import Company


class ConsoleScreen:
    def getCompanyInfo():
        name = input("이름 : ")
        addr = input("주소 : ")
        ceo = input("사장 : ")
        emp = input("직원수 : ")
        return Company(name, addr, ceo, emp)
    
    def printResult(company):
        print("-------------")
        print(company.insertResult)
