import pandas as pd

a = pd.read_csv(
    "C:/Choi/subway.csv", sep=",", names=["년", "월", "일", "호선", "역", "탄", "내린"]
)

#  데이터 어떻게 생겼나 잘 모르겠음 -> 마지막 데이터 3개만
print(a.tail(3))
print("-----")

# 언제부터 모은 데이터인가 -> 첫 데이터만 날짜만
print(a.head(1)[["년", "월", "일"]])
print("-----")

# 100 ~ 110번 데이터 노선번호, 역이름
print(a.iloc[100:111][["호선", "역"]])
print("-----")

# 노선번호로 찾을수있게
a = a.set_index(a["호선"])
print(a.loc["1호선"])
print("-----")

# 3호선 데이터만
print(a[a["호선"] == "3호선"])
print("-----")

# 2호선 데이터의 역명, 탄, 내린
print(a[a["호선"] == "2호선"][["역", "탄", "내린"]])
print("-----")

# 탄 사람수가 50000명 이상인 데이터
print(a[a["탄"] > 50000])
print("-----")

# 내린 사람수가 50이 안되는 거 날짜, 역명
print(a[a["내린"] < 50][["년", "월", "일", "역"]])
print("-----")

# 종각역 데이터
print(a[a["역"] == "종각"])
print("-----")

# 역명에 입구들어가는 데이터
print(a[a["역"].str.contains("입구")])
#                   startswith
#                   endswith
print("-----")

# 역명이 서울로 시작하는 데이터 역명, 탄, 내린
print(a[a["역"].str.startswith("서울")][["역", "탄", "내린"]])
