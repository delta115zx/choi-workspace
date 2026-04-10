# 숫자를 1개 넣으면
# 1 + 2 + 3 + ... + 그 숫자 = ?
# 함수

# 함수 recursive call(재귀적 호출)
#   함수 속에서 자기 자신을 호출해서 반복이 생기게 하는 테크닉

def getSum(x):
    if x == 1:
        return 1
    else:
        return getSum(x - 1) + x
##################################
a = getSum(4)
print(a)
