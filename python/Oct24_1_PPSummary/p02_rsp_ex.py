from random import randint
########################################
def printRule(handTable):
    for i, v in enumerate(handTable):
        if i != 0:
            print("%d. %s" % (i, v))
    print("-----")
 
def userFire():
    userHand = int(input("뭐 : "))
    if 0 < userHand < 4:
        return userHand
    return userFire()
 
def comFire():
    return randint(1, 3)
 
def printHand(handTable, comHand, userHand):
    print("컴 : %s" % handTable[comHand])
    print("나 : %s" % handTable[userHand])
 
def judge(comHand, userHand):
    t = userHand - comHand
    if t == 0:
        print("무")
        return 0
    elif t == -1 or t == 2:
        print("패")
        return 346345423
    else:
        print("승")
        return 1
########################################
handTable = [None, "가위", "바위", "보"]
 
printRule(handTable)
 
win = 0
while True:
    userHand = userFire()
    comHand = comFire()
    printHand(handTable, comHand, userHand)
    result = judge(comHand, userHand)
    if result == 346345423:
        print("%d연승" % win)
        break
    win += result
    print("-----")
 