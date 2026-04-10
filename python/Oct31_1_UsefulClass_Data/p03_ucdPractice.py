# 1) snack.csv읽어서 한줄씩 콘솔출력
# 2) 이름따로 가격따로...
# 3) 과자(이름, 가격, 중량, 정보출력) 표현할 준비
# 4) 객체 list
# ?) 제일비싼과자 정보, 각 과자 g당 가격, ...
class Snack:
    def __init__(self, line):
        line = line.replace("\n", "")
        line = line.split(",")
        self.name = line[0]
        self.price = line[1]
        self.weight = line[2]

    def printInfo(self):
        print(self.name, self.price, self.weight)


#########################################
f = open("C:\\Choi\\snack.csv", "r", encoding="utf-8")
snacks = []
for line in f.readlines():
    s = Snack(line)
    snacks.append(s)
f.close()

# 전체과자 정보출력
for s in snacks:
    s.printInfo()
print("-----------")

# 제일 비싼 과자 정보출력 -> 가격 비싼순 정렬
snacks.sort(key=lambda s: s.price, reverse=True)
snacks[0].printInfo()
print("------------")

# g당 가격이 가장 싼 과자 정보출력 -> g당 가격 싼순 정렬
snacks.sort(key=lambda s: (int(s.price) / float(s.weight)))
snacks[0].printInfo()

