# CPU(연산장치) -> 연산이 빠름
# RAM(변수형태로 임시저장장치) -> 많이 저장가능
# HDD/SSD(파일형태로 영구저장장치) -> 많이 저장가능
# GPU(그래픽처리용 CPU+RAM+HDD)

# 1) 띄어쓰기는 무의미
# 2) 띄어쓰기도 글자
# 3) 글자 한글자 쓸때마다 프로그램 용량 증가
# 4) 한글자당 2byte

# 소스 한 글자라도 덜 쓸 궁리
# 옛날 컴 사양이 낮아서 -> 알고리즘의 시대
# 요즘에는 컴 사양이 좋아져서 아껴봐야 의미가 -> 유지보수의 시대

# 연산자(operator)
#   = 우항에 있는거 좌항에 넣어라

# "어쩌고" : 글자데이터
# 어쩌고 : 파이썬 문법

# 변수(variable)
#   데이터를 임시로 저장하는 공간(그릇)
#   문법
#       변수명 = 데이터

#   변수명(그릇이름) : 자유롭게 지으면됨
#       규칙
#           파이썬 문법은 사용불가
#           숫자로 시작불가
#           특수문자 사용불가(몇몇 예외는 있음(_))
#       문화
#           뜻이 통하게
#               길어도 좋으니
#           한글 자제
#           대문자로 시작을 안했으면...(대부분의 다른 언어)

a = 10  # a라는 변수를 만들어서 10을 저장해
print("a")
print(a)

# 정수형 데이터
# 식당 테이블수 10이라는 데이터가 생김, 임시 저장
restaurantTableCount = 10  # 낙타체
# restaurant_table_count = 10 # 뱀체(Python에서 선호)
print(restaurantTableCount)

# 실수형 데이터
# 식당 별점이 4.3이라는 데이터가 생김, 임시 저장
restaurantRating = 4.3
print(restaurantRating)

# 글자 데이터
# 식당 이름이 김밥천국종로점이라는 데이터가 생김, 임시 저장
restaurantName = "김밥천국종로점"
print(restaurantName)

# 논리형 데이터(식당 영업중/아닌지)
# 식당 영업중임이라는 데이터가 생김, 임시 저장
restaurantIsOpened = True
# restaruantIsOpened = False
print(restaurantIsOpened)

