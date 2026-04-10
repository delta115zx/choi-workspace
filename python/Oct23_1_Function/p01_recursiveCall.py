# 숫자 하나 넣으면 팩토리얼 구하는 함수
# 1! = 1 = 1
# 2! = 1 x 2 = 2
# 3! = 1 x 2 x 3 = 6


# getFact(1) = 1
# getFact(2) = getFact(1) x 2 = 1 x 2
# getFact(3) = getFact(2) x 3 = getFact(1) x 2 x 3 = 1 x 2 x 3
def getFactorial(n):
    if n == 1:
        return 1
    return getFactorial(n - 1) * n


#####################################
a = getFactorial(5)
print(a)

print("-----")


# 숫자를 하나 넣으면 그 위치의 피보나치수열 값 구하는 함수
# 1 2 3 4 5 6 7 - 위치
# 1 1 2 3 5 8 13- 값

# getFibo(4)
#   return getFibo(2) + getFibo(3)
#          return 1     return getFibo(1) + getFibo(2)
#                              return 1     return 1
def getFibo(n):
    if (n == 1) or (n == 2):
        return 1
    return getFibo(n - 2) + getFibo(n - 1)

b = getFibo(7)
print(b)
