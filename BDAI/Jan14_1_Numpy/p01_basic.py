# anaconda
#   Python + BD/AI에 유용한 라이브러리 다 설치된 가상환경
#   +
#   Jupyter Notebook이라는 작업 툴
#       -> 대화형 처리 가능 : 한줄써서 실행해보고...
#       -> 분석스러운 작업에 적합

# Numpy, Pandas
# Python이 OOL라는걸 너무신경안씀

# 1) 설치수업?
# 2) 굳이 가상환경?
# 3) 분석/AI만x 완성된 프로그램까지 만들게
# 4) MS Azure MachineLearning에서 그런 환경 제공해 줌
#############
# 대량의 데이터들 -> 컬렉션(list, set, dict, ...)
#   -> 더 좋은 컬렉션
# NumPy : Python 빅데이터 분석 라이브러리
#           -> Python 빅데이터 관리 라이브러리
#           -> 주로 사용하는건 np.array : 좋은 list
# pip install numpy
#############
score = [[100, 90, 30], [50, 30, 80]]
print(score)
print(type(score))
print(score[0])
print(score[0][1])
# score[1][2] = 0 # 두번째학생 수학점수 0점으로
# 두번째학생 다 0점으로
# score[1][0:3] = 0 # 한꺼번에 데이터 여러개 수정이 불가능
print(score)
print("-----")

import numpy as np

score2 = np.array(score)
print(score2)  # 가독성이 올라갔나?
print(type(score2))
print(score2[0])
print(score2[0][1])  # 기존 list스타일
print(score2[0, 1])  # NumPy스타일
# score2[1, 2] = 100
score2[1, 0:3] = 100  # slicing : 한꺼번에 데이터 여러개 수정 가능
print(score2)
print(score2.shape)  # 몇행몇열
print(score2.dtype)  # 데이터의 자료형
print(len(score2))
print(score2.size)  # 데이터 몇개

# OOL에서 다차원list를 쓰나 -> NumPy굳이?
# -> TensorFlow/PyTorch... 후속기술들이 NumPy를 써서