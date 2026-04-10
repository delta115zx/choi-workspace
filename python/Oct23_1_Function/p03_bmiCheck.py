# 이름 :
# 키 :
# 몸무게 :
# --------------
# BMI : 21.40
# 홍길동씨는 고도비만

from time import sleep

def getHeight():
    height = float(input("키(m단위) : "))
    if height < 3:
        return height
    return getHeight()

def getWeight():
    weight = float(input("몸무게 : "))
    if weight > 300:
        return weight
    return getWeight()

def getName():
    name = input("이름 : ")
    return name


name = getName()
height = getHeight()
weight = getWeight()
bmi = weight / (height**2)
print("---------------")
print("BMI : %.2f" % bmi)
# if bmi >= 39:
#     print("%s씨는 고도비만" % name)
# elif bmi >= 32:
#     print("%s씨는 중도비만" % name)
# elif bmi >= 30:
#     print("%s씨는 경도비만" % name)
# elif bmi >= 24:
#     print("%s씨는 과체중" % name)
# elif bmi >= 10:
#     print("%s씨는 정상" % name)
# else:
#     print("%s씨는 저체중" % name)

result = "저체중"
if bmi >= 39:
    result = "고도비만"
elif bmi >= 32:
    result = "중도비만"
elif bmi >= 30:
    result = "경도비만"
elif bmi >= 24:
    result = "과체중"
elif bmi >= 10:
    result = "정상"
print("%s씨는 %s" % (name, result))

sleep(10)

# 일반인들이 실행하기 용이하게
# 실행파일까지 만들어줘야
# 1) bat파일
# 2) pyinstaller

# .bat
#   cmd명령어 써놓는 파일
#   실행하면 그 명령어가 실행됨