from operator import index
import pandas as pd

df = pd.read_csv("C:/Choi/titanic.csv")
df = df.set_index(df["Name"])
print(df)
print("-----")

# index 기준 정렬
# df = df.sort_index()
df = df.sort_index(ascending=False)
print(df)
print("-----")

# 필드명 순 정렬
df = df.sort_index(axis=1)
print(df)
print("-----")

# index이외의 필드로 정렬
# df = df.sort_values(by="Age")
# df = df.sort_values(by=["Pclass", "Age"])
df = df.sort_values(by=["Pclass", "Age"], ascending=[False, True])
print(df[["Pclass", "Age"]])
print("-----")

# 반복문으로 전체
# print(df.index)
for n in df.index:
    print(df.loc[n])
    print("-----")