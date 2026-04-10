# OOD(Object-Oriented Design)
#   객체지향프로그래밍 스타일 설계
#   1) OOP : 프로그램소스로 리얼월드 묘사하자
#       -> 비만센터에 가서 실제로 비만도검사하는 씬을 떠올리자
#   2) 만들 프로그램에 필요한것만 남겨서 객체로 표현할 준비(등장인물)
#       -> 의사, 손님
#   3) 각 객체의 속성(필요한것만)
#   4) 씬 재생 -> 각 객체들의 액션이 보이겠는데
#   5) 만들어가기

# 변수
#   전역변수 :
#   지역변수 : 그 행동 하는동안만 필요한
#   파라메터 : 그 행동하는데 필요한 재료(의사한테 붙어있는거 말고)
#   멤버변수 : 객체의 속성


class Doctor:
    def start(self):
        patient = self.callPatient()  # 업무 보는동안만 의미있는 손님
        self.ask(patient)
        self.calculate(patient)
        self.tellResult(patient)

    def callPatient(self):
        # return 이 행동하고나서 생기는거
        return Patient()  # 손님을 부르고 나면 -> 손님이 생김

    def ask(self, patient):
        patient.tell()

    def calculate(self, patient):
        if patient.height > 3:
            patient.height /= 100
        patient.bmi = patient.weight / (patient.height * patient.height)

        if patient.bmi >= 39:
            patient.result = "고도비만"
        elif patient.bmi >= 32:
            patient.result = "중도비만"
        elif patient.bmi >= 30:
            patient.result = "경도비만"
        elif patient.bmi >= 24:
            patient.result = "과체중"
        elif patient.bmi >= 10:
            patient.result = "정상"

    def tellResult(self, patient):
        print("BMI : %.2f" % patient.bmi)
        print("%s씨는 %s" % (patient.name, patient.result))


# name이라는 변수
class Patient:
    def tell(self):
        self.name = input("이름 : ")
        self.height = float(input("키(m) : "))
        self.weight = float(input("몸무게 : "))


########################
d = Doctor()
d.start()
