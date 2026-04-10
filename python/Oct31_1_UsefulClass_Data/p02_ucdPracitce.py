# csv(comma separated value)
#   값이 ,로 구분
#   엑셀에서 열리기는 하는데 -> MS Office가 utf-8을 소화못함(euc-kr은 정상)
f = open("C:\\Choi\\snack.csv", "a", encoding="utf-8")
while True:
    name = input("이름 : ")
    if name == "그만":
        break
    price = int(input("가격 : "))
    weight = float(input("중량 : "))
    print("-------")
    f.write("%s,%d,%.1f\n" % (name, price, weight))
f.close
