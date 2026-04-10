from os import replace
import pandas as pd

df = pd.read_csv("C:/Choi/titanic.csv")
df = df[["Name", "Sex"]]  # 이름, 성별만

# 성별필드에서 male -> 남, female -> 여
df["Sex"] = df["Sex"].replace(["male", "female"], ["남", "여"])


# 쌩Python 함수
def convertMr(name):
    return name.replace("Mr.", "미스터")




# 이름필드에서 Mr. -> 미스터
# df["Name"] = df["Name"].replace("Mr.", "미스터")
df["Name"] = df["Name"].apply(convertMr)

# 이름필드에서 성 날리고, 이름만
# def removeFamilyName(name):
#     return name.split(", ")[0]
df["Name"] = df["Name"].apply(lambda name: name.split(", ")[0])

print(df)
