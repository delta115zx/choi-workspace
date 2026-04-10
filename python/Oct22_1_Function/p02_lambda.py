# 일반함수
#   소스정리    : 만들어놓고 여러번쓰게
#   parameter   : 함수 실행에 필요한 재료
#   return      : 함수 결과물 돌려주는
# lambda함수    : 무명의 1회용 함수
#   언제 - 값 간단하게 구할때
#   (lambda param변수명, param변수명, ...:내용)(값)

# 자기 이름 출력하는 함수
# def printMyName(n):
#     print(n)
# 사용
# printMyName("최진영")
(lambda n: print(n))("최진영")

print("------")

# lambda함수는 애초에 값 구하는 용도
# -> 그냥 값만 던져놓으면 return으로 작동
d = (lambda a, b, c: (a + b + c) / 3)(10, 20, 55)
print(d)

# 숫자 3개 넣으면, 그 평균값 구해주는 함수
# def getAverage(a, b, c):
#     # average = (a + b + c) / 3
#     # return average
#     return (a + b + c) / 3


# # 10, 20, 55의 평균값
# o = getAverage(10, 20, 55)
# # 출력
# print(o)
