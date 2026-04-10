# Garbage Collection : heap영역 자동정리 시스템
#   그 자동이 발동 시점 : 그 번지를 가리키는 변수가 없게 되면

# 어쨋든 Python프로그램은 프로그램 종료시 정리는 다 됨
# 빅데이터를 다뤄야 -> 정리를 빨리 해 줄 필요가
##################################
# RAM : 변수형태로 임시저장공간(컴 끄면 삭제) 
#   OS가 논리적인 3가지 공간으로 나눠서 사용
#   static
#   stack : 용량작은게 저장, 규칙적인 용량이 저장
#           -> 밑에서부터 차례차례 공간 사용
#           프로그램 종료시 정리됨
#   heap : 용량큰게 저장, 사이즈가 다 천차만별
#           -> 컴이 적당하다 싶은 공간 사용
#           자동정리x, 개발자가 정리해야
#######################
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self):
        print("학생 없어짐")

    def printInfo(self):
        print(self.name, self.age)
        print("----------")


#######################
# 이름이 홍길동, 나이가 20살인 학생
# 정보출력

s1 = Student("홍길동", 20)
s1.printInfo()
# 이름이 길길동, 나이가 22살인 학생
# 정보출력
s2 = Student("김길동", 22)
s2.printInfo()

# 연산자 = stack영역대상

# s1이랑 이름이 같고, s1이랑 나이가 같은 세번쨰 학생 - x
s3 = s1 # s1학생을 s3로도 부를수있게
s3.printInfo()

# s1이 이름을 홍길도로 개명
s1.name = "홍길도"
s1.printInfo()

s3.printInfo()

s1 = None
s3 = None
print("ㅋㅋㅋㅋㅋ")