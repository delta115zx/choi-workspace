from random import randint

turn = 0
################################
def getUserAns():
    userAns = int(input("뭐 : "))
    if 0 < userAns < 10001:
        return userAns
    return getUserAns

def pickGameAns():
    return randint(1, 10000)

# 판정하고나서, 게임 계속해야하는지 여부가 리턴되는 함수
def judge(gameAns, userAns):
    global turn
    turn += 1
    if  gameAns == userAns:
        print("%d턴만에 정답" % turn)
        return False
    elif gameAns > userAns:
        print("UP")
    else:
        print("DOWN")
    return True
################################
gameAns = pickGameAns()
print(gameAns)

while True:
    userAns = getUserAns()
    go = judge(gameAns, userAns)
    if not go:
        break
