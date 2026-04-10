from re import split
import pandas as pd

# 타이타닉
# 나이 -> 10대/20대/...
# 이름, 나이, 생존여부만

df = pd.read_csv("C:/Choi/titanic.csv")
df = df[["Name", "Age", "Survived"]]
df["Age"] = df["Age"].fillna(999)


# def convertAge(age):
#     if age == "몰라":
#         return age
#     elif age < 10:
#         return age
#     else:
#         age = str(age)
#         return age[0] + "0대"

df["Age"] = df["Age"].apply(lambda age: "%d0대" % (age // 10))
df["Age"] = df["Age"].replace("990대", "미상")
print(df)
