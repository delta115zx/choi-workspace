import pandas as pd

df = pd.read_csv("C:/Choi/titanic.csv")
print(df)
print("-----")
# 등급별 평균요금
print(df.groupby("Pclass")["Fare"].mean())
print("-----")

# 등급별 산/죽은 사람 수
print(df.groupby(["Pclass", "Survived"])["PassengerId"].count())
print("-----")

# 성별별 산/죽은 사람 수
print(df.groupby(["Sex", "Survived"])["PassengerId"].count())
print("-----")

# 나이대별 -> 성별별 산/죽은 사람 수
df["Age2"] = df["Age"].fillna(999)
df["Age2"] = df["Age2"].apply(lambda age: "%d0대" % (age // 10))
df["Age2"] = df["Age2"].replace("990대", "미상")
print(df.groupby(["Age2", "Sex", "Survived"])["PassengerId"].count())

# 객실 뭐뭐있나(중복제거)
print(df["Cabin"].unique())
print("-----")

# 객실 몇개(중복제거해서 몇개)
print(df["Cabin"].nunique())
print("-----")

# 객실별 몇명씩
print(df["Cabin"].value_counts())
print("-----")

# 시장
df2 = pd.read_csv("C:/Choi/LNPS.csv", names=["마트", "품명", "가격", "날짜", "종류", "구"])

# 시장이 뭐뭐있나
print(df2["마트"].unique())
print("-----")

# 시장이 몇종류
print(df2["마트"].nunique())
print("-----")

# 구별 데이터 몇개씩
print(df2["구"].value_counts())
print("-----")