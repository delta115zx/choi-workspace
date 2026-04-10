# 예외처리
#   try:
#       내용
#   except 이름:
#       대응
#   except 이름:
#       대응
#   ...
#   -> 내용부분 하다가 문제없으면 없음
#   -> 내용부분 하다가 예외가 발생하면 대응쪽으로 이동
x = int(input("x : "))
y = int(input("y : "))
z = [234, 123, 132454]
print("------")

# try:
#     d = x / y
#     print(d)
#     print(z[y])
# except ZeroDivisionError:
#     print("나누기 0은 없다")
# except IndexError:
#     print("list에 그거 없음")

# try:
#     d = x / y
#     print(d)
#     print(z[y])
# except:
#     print("어쨌든 문제 발생")

try:
    d = x / y
    print(d)
    print(z[y])
except Exception as e:
    print(e)
    print("어쨌든 문제 발생")
