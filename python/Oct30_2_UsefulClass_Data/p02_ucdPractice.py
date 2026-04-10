class Calculator:
    def getData():
        pass

    def calc():
        pass
#####################
l = input("숫자(x,y,z,...) : ")

l = l.split(",")

    
sum = 0
for i in range(len(l)):
    sum += int(l[i])
print(sum)

avg = sum / len(l)
print(avg)
