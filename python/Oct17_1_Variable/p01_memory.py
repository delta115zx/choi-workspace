# Python : 메모리 관리 + 자료형 자동
# Java : 메모리 관리 자동, 자료형은 사람이 직접
# C언어 : 메모리 관리 사람이 직접

# HDD/SSD : 영구저장장치
# RAM : 임시저장장치
#   OS가 논리적으로 나눠서 관리
#   static
#   stack - 아래쪽에서부터 쌓아나가는 형태로
#           변수는 무조건 여기
#   heap - OS가 적당하다 싶은 위치를 사용

# 컴퓨터가 32bit/64bit -> 주소값 저장된 변수사이즈
# 컴이 32bit면 램이 4GB이상 못쓴다
#   -> 주소값 저장된 변수사이즈가 작아서 큰 번지값을 저장 못해서

# Python은 변수는 stack에, 데이터는 heap에

# 과자이름이 다이제미니
# 자료형
# 과자이름 출력

snackName = "다이제미니"
print(id(snackName))    # id(변수명) : 메모리 번지값
print(type(snackName))  # type(변수명) : 자료형
print(snackName)
print("-------------")

# 과자가격이 5000원
# 자료형
# 과자가격 출력

snackPrice = 5000
print(id(snackPrice))
print(type(snackPrice))
print(snackPrice)
