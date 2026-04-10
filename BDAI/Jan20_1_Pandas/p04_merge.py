import pandas as pd

df1 = pd.read_csv("C:/Choi/titanic.csv")
df2 = pd.read_csv("C:/Choi/titanic.csv")

df3 = pd.concat([df1, df2])  # df1뒤에 df2붙이기(데이터 추가)
print(df3)
print("-----")

df4 = pd.concat([df1, df2], axis=1)  # df1옆에 df2붙이기(join인데...)
print(df4)
print("-----")

snack = pd.DataFrame()
snack["이름"] = ["새우깡", "빼빼로"]
snack["가격"] = [3000, 2000]
snack["제조사"] = ["농심", "롯데"]
# snack["위치"] = ["1번", "카운터옆"]

company = pd.DataFrame()
# company["제조사"] = ["농심", "롯데"]
company["회사명"] = ["농심", "롯데"]
company["위치"] = ["서울", "제주"]

# 양쪽 다 제조사라는 필드
# dfdf = pd.merge(snack, company)
# print(dfdf)

# 양쪽 다 존재하는 필드가 여러개
# dfdf = pd.merge(snack, company, on="제조사")
# print(dfdf)

# 양쪽 필드명 다르면
dfdf = pd.merge(snack, company, left_on="제조사", right_on="회사명")
print(dfdf)