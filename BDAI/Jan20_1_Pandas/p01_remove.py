import pandas as pd
import numpy as np

df = pd.read_csv("C:/Choi/titanic.csv")
print(df)
print("-----")
# print(df.columns)
# Pandas : 원본데이터에 영향 안가는걸 추구
# 에서 삭제가 의미가 있나

df = df.drop("Survived", axis=1) # Survived 필드 삭제
df = df.drop(["Pclass", "Fare"], axis=1) # Pclass, Fare 필드 삭제
# PassengerId, Sex, SibSp, Parch, Ticket, Cabin, Embarked -> Name, Age만 가져오기
df = df[["Name", "Age"]]
print(df)
print("-----")

df = df.drop(889) # 889번 삭제x, index가 889인거 삭제
df = df.set_index(df["Name"])
df = df.drop("Dooley, Mr. Patrick")
# df = df.loc["Graham, Miss. Margaret Edith"] # Graham, Miss. Margaret Edith 빼고 다 삭제
df = df[df["Age"] < 30] # 나이가 30이상인거 다 삭제
print(df)
print("-----")

# 모기
df = pd.read_csv("C:/Choi/mosquito.csv", names=["날짜", "물가", "집", "공원"])

# 물가, 공원필드 없애고
df = df.drop(["물가", "공원"], axis=1)
print(df)
print("-----")

# 미측정된거 없애고
# df["집"] = df["집"].replace("noValue", np.nan)
df = df[df["집"] != "noValue"]
df["집"] = pd.to_numeric(df["집"])

# 전체조회
print(df)
print("-----")

# 새로 생긴 df의 자료형을 왜 그대로 뒀을까
# 집 모기지수 평균값
print(df["집"].mean())

# pandas는 원본에 영향안가는걸 추구
# -> 안전하네, GC는...