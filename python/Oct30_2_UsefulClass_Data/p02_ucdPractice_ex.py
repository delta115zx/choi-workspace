numbers = input("숫자(x,y,z,...) : ")
print("------------")

numbers = numbers.split(",")


hab = 0
cnt = len(numbers)
for n in numbers:
    try:
        hab += int(n)
    except:
        cnt -= 1
print("합계 : %d" % hab)
print("평균 : %.2f" % (hab / cnt))

