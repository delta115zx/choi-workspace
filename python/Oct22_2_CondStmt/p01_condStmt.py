# 프로그램 : 위 -> 아래, 왼 -> 오른
# 프로그램 실행순서를 바꿔야할때가
#   제어문
#       조건문
#       반복문

# 조건문(Conditional Statement) : 조건 따져서 실행할지말지
#   다른 PL들 : if, switch
#   Python : if

# if 조건식A:    # 조건식 쓸때 가독성 차원에서 () 사용가능
#   A를 만족시키는 경우에 여기 실행
# elif 조건식B:
#   A는x, B는 만족시키는 경우에 여기
# elif 조건식C:
#   A/Bx, C는 만족시키는 경우에 여기
# ...
# else:
#   위에 만족되는거 하나도 없으면

mid = int(input("중간고사 : "))
final = int(input("기말고사 : "))
avg = (mid + final) / 2
print("--------")
print("평균점수 : %.1f" % avg)

# interpreter방식 언어 : 위에서부터 한줄씩 실행
#                       30번줄 실행될떄 a라는 변수가 있기만 하면 됨

# 평균점수가 90점 이상이면 잘했다
# if avg >= 90:
#     print("잘했다")
#     a = 10

# print(a)

# 평균점수가 80점 이상이면 잘했다
# 80점 안되면 나가
#   근데 70은 넘겼으면 열심히해라
if avg >= 80:
    print("잘했다")
else:
    print("나가")
    if avg >= 70:
        print("열심히해라")

# 점수가 90점 이상이면 수
# 80 <= 점수 < 90이면 우
# 70 <= 점수 < 80이면 미
# ...
if avg >= 90:
    print("수")
elif avg >= 80:
    print("우")
elif avg >= 70:
    print("미")
elif avg >= 60:
    print("양")
else:
    print("가")