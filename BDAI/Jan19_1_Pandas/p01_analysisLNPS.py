import pandas as pd
import numpy as np

# 그거 불러서 df
f = pd.read_csv(
    "C:/Choi/LNPS.csv", names=["마트", "품명", "가격", "날짜", "종류", "구"]
)
f["품명"] = f["품명"].replace("?", np.nan)
f["품명"] = f["품명"].fillna("몰라")
f["마트"] = f["마트"].fillna("몰라")

# 마트이름으로 찾을수있게
f = f.set_index(f["마트"])

# 마트이름 가나다순 정렬
f = f.sort_index()

# 전체출력
print(f)
print("-----")

# 통인시장 데이터만
print("-----")
print(f.loc["통인시장"])

# 마트명에 '가락' 들어있는 데이터만
print("-----")
print(f[f["마트"].str.contains("가락")])

# 사과는 어떤 마트에서 살 수 있나
print("-----")
print(f[f["품명"].str.contains("사과")][["마트"]])

# 품명 가나다 -> 가격 비싼순 정렬
print("-----")
f = f.sort_values(by=["품명", "가격"], ascending=(True, False))
print(f)


print(f[f["품명"] == "몰라"])
print("-----")
# 전체출력
# print("-----")
# for n in f.index:
#     print(f.loc[n])
#     print("-----")

# 30000원 이상인 데이터 품명, 가격
print(f[f["가격"] >= 30000][["품명", "가격"]])

# 종로구 데이터만 반복문으로 하나하나 출력
jongroDF = f[f["구"] == "종로구"]
for i, v in enumerate(jongroDF.index):
    print(jongroDF.iloc[i])
    print("------")