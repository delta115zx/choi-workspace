# 폰 모델명 입력받아
# 출력
phoneModelName = input("폰 모델명 : ")
print("폰 모델명은 %s입니다." % phoneModelName)
print(id(phoneModelName), type(phoneModelName))
print("-----------")


# 형변환(type casting) : 자료형을 바꿔주는
#   자료형(변수명)

# 사용자가 글자를 입력할지 숫자를 입력할지 모름
# Python입장에서 price변수 자료형을 골라줄때
#   십만원, 100000를 다 소화할수있는걸로 골라줘야 -> str

# 폰 가격 입력받아
# 출력
# 주소, 자료형
phonePrice = input("폰 가격 : ")
phonePrice = int(phonePrice)
print("폰 가격은 %d입니다." % phonePrice)
print(id(phonePrice), type(phonePrice))
print("--------")
# 화면크기 입력받아서
# 무조건 소수점이하 2자리로 나오게 출력
# 컴 사양은 좋고
# 어쨌든 변수 안쓸수있다면 안쓰면 좋은거 : 메모리 사용량 줄고
# 어쨌든 소스 짧으면 좋은거 : 프로그램 용량 줄고
# -> 소스 가독성이 너무 박살나지 않는 선에서 줄여서 쓰자
displaySize = float(input("화면크기 : "))
print("화면 크기는 %.2f인치입니다." % displaySize)


phoneDisplaySize = float(input("폰 화면크기 : "))
print("폰 화면크기는 %.2f인치입니다." % phoneDisplaySize)
