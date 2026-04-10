
import math


class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def printInfo(self):
        print(self.name, self.korean, self.english, self.math)
    

####################
# 이름이 홍길동, 국어100, 영어90, 수학80 학생
# 정보출력

s1 = Student("홍길동", 100, 90, 80)
s2 = Student("김길동", 50, 100, 100)
score = [
    s1,
    s2,
    Student("최길동", 0, 0, 0),
    Student("이길동", 20, 30, 40),
    Student("박길동", 15, 25, 35),
]

score[0].printInfo() # 첫번째 학생의 모든정보출력(메소드 활용)
print(score[2].korean) # 세번째학생의 국어점수(소스 알아보기 쉽고)
print("--------")

# 학생객체를 넣으면, 학생의 이름이 리턴되는 함수
# def getName(s):
#     return s.name
# test = getName(score[2])
# print(test)

# test = (lambda s:s.name)(score[2])
# print(test)

# 정렬(이름 가나다순)
# score라는 list에는 학생객체가
# 정렬은 학생이름
# 학생객체를 넣으면 그 학생이름
# score.sort(key=lambda s:s.name)

# 정렬(평균점수 낮은순)
# test = (lambda s:(s.korean + s.english + s.math) / 3)(score[1])
# print(test)

score.sort(key=lambda s:s.korean + s.english + s.math, reverse=True)


print("------")
for s in score:
    s.printInfo()