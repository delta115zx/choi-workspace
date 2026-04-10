# 변수
#   전역변수 :
#   지역변수 : 그 행동 하는동안만 필요한
#   파라메터 : 그 행동하는데 필요한 재료(의사한테 붙어있는거 말고)
#   멤버변수 : 객체의 속성
from random import randint


class Com:
    def ask(self, user):
        userAnsTemp = user.tell()
        if 0 < userAnsTemp < 10001:
            return userAnsTemp
        return self.ask(user)

    def judge(self, gameAns, userAns):
        if userAns == gameAns:
            print("정답")
            return False
        elif userAns < gameAns:
            print("UP")
        else:
            print("Down")
        return True

    def tellResult(self, turn):
        print("%d턴만에 정답" % turn)

    def pickGameAns(self):
        return randint(1, 10000)

    def welcomeUser(self):
        return User()

    def start(self):
        turn = 0
        user = self.welcomeUser()
        gameAns = self.pickGameAns()
        print(gameAns)
        while True:
            turn += 1
            userAns = self.ask(user)
            if not self.judge(gameAns, userAns):
                break
        self.tellResult(turn)


class User:
    def tell(self):
        return int(input("뭐 : "))


#########################
c = Com()
c.start()
