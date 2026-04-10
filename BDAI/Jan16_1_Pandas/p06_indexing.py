import pandas as pd

a = pd.read_csv("C:/Choi/titanic.csv")

# 기본정보
print(a)
print("-----")
print(a.shape)
print("-----")
print(a.columns)
print("-----")
print(a.head())
print("-----")
print(a.tail(3))
print("-----")

# 열 기준 조회(특정 필드만 -> select ???)
print(a["Name"])
print("-----")
print(a.Name)
print("-----")
print(a[["Name", "Age"]])
print("-----")

# 행 기준 조회(특정 데이터만 -> where ???)
print(a.iloc[1])  # 1번 데이터
print("-----")
print(a.iloc[1:5])  # 1 ~ (5-1)번 데이터
print("-----")
# index : 찾는 기준(primary key) - 기본은 0,1,2,3,...
a = a.set_index(a["Name"])
print(a)
print("-----")
print(a.loc["Dooley, Mr. Patrick"])
print("-----")
print(a.loc["Montvila, Rev. Juozas":"Dooley, Mr. Patrick"])
print("-----")

# 행+열(select ??? ... where ???)
print(a.loc["Dooley, Mr. Patrick"]["Age"])
print("-----")
print(a.loc["Dooley, Mr. Patrick"][["Pclass", "Age"]])
print("-----")
print(a.loc["Dooley, Mr. Patrick", "Age"])
print("-----")
print(a.loc["Dooley, Mr. Patrick", ["Pclass", "Age"]])
print("-----")

# 조건(where ???)
# print(a["Age"])
# print(a["Age"] > 30)
print(a[a["Age"] > 30]["Age"])
print("-----")

# 20대
# 이름, 나이, 등급
print(a[(a["Age"] >= 20) & (a["Age"] < 30)][["Age", "Pclass"]])
