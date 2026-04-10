from random import randint


class Friend:

    def getHandtable(self):
        return [None, "가위", "바위", "보"]

    def callUser(self):
        return User()
    
    def printRule(self, handTable):
        for i, v in enumerate(handTable):
            if i != 0:
                print("%d. %s" % (i, v))
    

    def start(self):
        user = self.callUser()
        handTable = self.getHandtable()
        self.printRule()
        friendHand = self.friendFire()
        userHand = self.checkUserFire(user)
        self.nowHands(friendHand, userHand, handTable)
        self.judge(friendHand, userHand)

    def friendFire(self):
        return randint(1, 3)

    def checkUserFire(self, user):
        userHandTemp = user.userFire()
        if 0 < userHandTemp < 4:
            return userHandTemp
        return self.checkUserFire(user)

    def judge(self, friendHand, userHand):
        t = userHand - friendHand
        if t == 0:
            print("무")
        elif t == -1 or t == 2:
            print("패")
        else:
            print("승")

    def nowHands(self, friendHand, userHand, handTable):
        nowFriendHand = handTable[friendHand]
        nowUserHand = handTable[userHand]
        print("친구 : %s" % nowFriendHand)
        print("나 : %s" % nowUserHand)

    def tellResult(self):
        pass


class User:
    def userFire(self):
        return int(input("뭐 : "))


########################
f = Friend()
f.start()
