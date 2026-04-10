# Python은 모든 데이터가 다 객체

# str : 수정불가능한 문자열 객체

# s = str("뭐 이래요") 원래는 이렇게
s = "뭐 이래요"  # 약식으로 쓰는것도 허용
print(s)
print(type(s))  # class
print(id(s))  # 데이터가 저장되어있는 heap영역 주소값
# Python에는 형변환x -> 객체 만드는것 뿐

# Python으로 만든 변수의 자료형 : object

# 다형성(polymorphism) : 상위자료형 변수에 하위자료형 넣을수 있는
# 사람자료형 변수에 남자 넣는거
# 사람자료형 변수에 여자 넣는거
# Python은 다형성을 엄청 활용하는 언어
# 변수 s자료형이 object
#   s = "ㅋ"  # object변수에 str넣음
#   s = 10 # object변수에 int?
print("----------")

s = "키\t : %.2fcm" % 180.4564
print(s)

# 쓴모양 그대로 나오게
s = """ㅋㅋㅋ
저렁게              쓸수가
        있는데요"""
print(s)

# 주석 : 기계어로 번역할떄 제외
"""
    근데 이렇게 해놓으면
    주석?
    str객체 만든거 -> 메모리공간 차지 
    -> 변수에 저장은 안했으니 GC
"""


class Dog:
    """
    설명서
    """

    def bark(self):
        """
        ㅎㅎㅎ
        """
        print("멍")


# help(Dog)
# help(str)

# 영어실력 + help + 툴
# Python : 자유 -> 하고싶으면 하는 OOP
#   Hybrid OOL -> 메소드형태가 아닌것도
#   대체할수있으면 삭제
s = "고기를 한번 잡아봐요"

# s가 고기를 이라는 말로 시작하는지
print(s.startswith("고기를"))

# s에서 한번 -> 두번으로 바꿔서
print(s.replace("한번", "두번"))

# s에서 잡 이 몇번째 위치에 있나
print(s.find("잡"))
# print(s.index("잡"))

# s에서 두번째 글자
print(s[1])

# s에 봐 라는 글자가 들어있
print(s.find("봐") != -1)

# s 글자수
print(len(s))

# 대량의 글자를 붙여나가
# -> 한번 붙일때마다 새로운 str객체 만드는
s = "자"
print(s, id(s))
s += " 뭘"
print(s, id(s))
s += " 붙여보죠"
print(s, id(s))

# 데이터 받아오면 str한덩어리
# -> 분리해서 사용
s = "홍길동,30,수원"
s2 = s.split(",")  # 분리해서 list로
print(s2)

# 데이터 받아오면
s = "               데이터              "
s2 = s.strip() # 앞뒤 공백 제거
print(s2)

s= "!!!!!!!!!!!!!!!데이터!!!!!!!!!"
s2 = s.strip("!") # 앞뒤 그거 제거
print(s2)

# 버전
#   1.9.13
#   1 : major
#   9.13 : minor

#   major버전이 0 : 미완성
#   major버전이 1 : 완성
#   1.9.13 -> 1.9.14 : 거의 체감안되는 변화
#   1.9.13 -> 1.10.0 : 뭔가 다름
#   1.9.13 -> 2.0.0 : 다른 프로그램
