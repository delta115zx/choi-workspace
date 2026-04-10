# static member variable
#   중복되는 데이터를 여러번 저장 안하게 -> 메모리 사용량 아껴주는
#   1) Python은 효율적인 프로그램 개발에 무관심
#   2) Python에도 smv같은게 있기는 한데, 다른언어처럼 극적인 효과가 없음
#   -> smv는 없는 취급

# static method
#   일반 method : 객체의 액션(객체가 있어야 사용가능)
#   static method : 객체가 없어도 쓸수있는 메소드
########################
# 변수 언제 만드나? - 데이터 임시저장할때
# 객체 언제 만드나? - 실생활스럽게 데이터 임시저장
# -> 무슨 데이터 저장
class Calculator:
    # 멤버변수 없음 -> 저장할거 없음 -> 객체 안만들어도 되겠네

    @staticmethod        # 가독성 + 개발툴중에 없으면 빨간줄처리하는 툴도 있음
    def printSum(x, y):  # 첫 파라메터로 self빼기
        print(x + y)


# ######################
# 클래스명.메소드(...)
Calculator.printSum(10, 30)
