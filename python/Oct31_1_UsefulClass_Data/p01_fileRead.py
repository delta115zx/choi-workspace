# 데이터 10TB -> 서버급컴 여러대 병렬 전처리 -> Python분석/AI
#                Hadoop : Linux에서만 실행가능한 Java

# Python
#   분석/AI관련 문법 쉽게 잘 만들어져있음
#   컴 자원을 낭비하는 경향

# encoding/decoding
#   전세계적으로 utf-8
#       Linux가 utf-8을 주력으로 써서
#       Windows가 euc-kr를 주력으로 쓰다가 -> utf-8쓰는쪽으로
#   국내에서는 euc-kr이 그 다음
f = open("C:\\Choi\\1030\\p05.txt", "r", encoding="utf-8")

# 1) 전체를 다 읽어서 str로
# data = f.read()
# print(data, type(data))

# 2) 다음 줄 읽어서 str로
# data = f.readline()
# print(data, type(data))
# data = f.readline()
# print(data, type(data))
# data = f.readline()
# print(data, type(data))

# 3) 전체를 다 읽어서, \n기준으로 나눠서 list로
# \n를 남겨놨음
data = f.readlines()
print(data, type(data))

f.close()