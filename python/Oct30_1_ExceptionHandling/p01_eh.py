# 예외처리
#   try:
#       내용
#   except 이름:
#       대응
#   except 이름:
#       대응
#   ...
#   else:
#       try부분 하는동안 아무문제 없으면
#   finally:
#       try부분 하는동안 문제가 있었든 없었든 무조건
#       return보다 먼저
try:
    x = int(input("x : "))
    y = int(input("y : "))
    z = x / y
    print(z)
except ValueError:
    print("잘못 입력")
except ZeroDivisionError:
    print("나누기 0은 없음")
else:
    print("정상계산 완료")
finally:
    print("어쨌든 여기는 무조건")
