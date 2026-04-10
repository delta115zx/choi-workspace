# 실무 프로젝트
# 고객
# PM
# back-end개발자1 : AI모델 개발
# back-end개발자2 : DB연동되는 부분 개발
# back-end개발자3 : PL
# front-end개발자1 : 앱 화면 개발
# front-end개발자2 : 웹 화면 개발
# front-end개발자3
# DBA1
# DBA2
# 디자이너1
# 디자이너2

# 저 많은 사람들이 하나의 프로그램 만들어 내는데
# 한 파일은 한 사람이 책임지고 작업하는게 작업이 용이
# -> 한 파일은 한 분야의 내용만 있어야 할 것

# MVC패턴 : 회사 실무 프로젝트의 기본
#   파일 나눠서 작업, 한 파일은 한 명이 끝까지 책임
#   파일이 하나 있으면 M/V/C중에 하나의 역할만
#   Model : 비즈니스 로직(실제 계산)
#   View : 실제로 사용자 눈에 보이는, 입력받고 결과 출력
#   Controller : 흐름 제어(View가 필요하면 View, Model필요하면 Model)

x = int(input("x : "))
y = int(input("y : "))
print("-----------")
z = x + y
print(z)

