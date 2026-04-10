import pandas as pd

a = pd.DataFrame()
a["이름"] = ["새우깡", "양파링"]
a["가격"] = [3000, 4000]
print(a)
print("-----")

# Pandas 1.x : append로 pd.Series, dict, ... 추가 가능
# Pandas 2.x : 혼란스럽다고 append삭제, df끼리 붙이기만 가능

s = pd.Series(["초코파이", 5000], index=["이름", "가격"])
# a = a.append(s)
s = pd.DataFrame([s])  # pd.Series -> pd.DataFrame
a = pd.concat([a, s])
print(a)
print("-----")

s = {"이름": "포카칩", "가격": 4000}
s = pd.DataFrame([s])
a = pd.concat([a, s])
print(a)
