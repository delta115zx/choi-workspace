# 프로그래밍언어에 어떤 기능이 만들어짐 2025/10/30
# 세월이 가고, 기술이 발전하면
#   2025/10/30시점에 만들어진 저걸 못쓰게 됨
#   -> 그 기능 고쳐야

# deprecated
#   그 기능 업그레이드/삭제/... 할 예정
#   유예기간
#       현재버전에서는 작동은 하는데
#       다음버전에서는 없어져도 몰라
#   -> 안쓰는쪽으로

# 패키지명 :
# 모듈명 : datetime.py
# 클래스명 : datetime
# today()의 정체 : static메소드
from datetime import datetime
from time import strftime

now = datetime.today()  # 현재시간날짜
print(now)
print(now.year)  # 연도만
print(now.month)  # 월
print(now.day)  # 일

# 특정시간날짜
d = datetime(1998, 1, 15)
print(d)


# d2 = input("날짜(yyyy/mm/dd) : ")

# d2.split("/")

# y = int(d2[0])
# m = int(d2[1])
# d = int(d2[2])

# d2 = datetime(y, m, d)
# print(d2)

# 패턴 확인
# help(strftime)

# str -> datetime
d3 = "2000/12/31"
d3 = datetime.strptime(d3, "%Y/%m/%d")
print(d3)

# 2025.10.30 15:53

# datetime -> str
d5 = datetime.today()
d5 = datetime.strftime(d5, "%Y.%m.%d.%H.%M")
print(d5)