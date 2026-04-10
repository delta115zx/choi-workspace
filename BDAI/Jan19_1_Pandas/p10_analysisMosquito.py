import pandas as pd
import numpy as np

df = pd.read_csv("C:/Choi/mosquito 1.csv", names=["날짜", "물가", "집", "공원"])
print(df)

# print(df[df["물가"].isnull()])  # 값이 없지는 않고
# print(df[df["물가"] == "noValue"])
# print(
#     df["물가"].dtype
# )  # 133.1, 135.8, noValue -> Pandas입장에서는 그거 다 소화가능한 object타입을 쓸 수 밖에
# print(df["물가"].mean())  # 자료형이 숫자가 아니니 -> 계산이...

# noValue -> 없애자
df["물가"] = df["물가"].replace("noValue", np.nan)
df["집"] = df["집"].replace("noValue", np.nan)
df["공원"] = df["공원"].replace("noValue", np.nan)
print(df["물가"].dtype)

# 필드 형변환
# ??? -> 숫자
df["물가"] = pd.to_numeric(df["물가"])
df["집"] = pd.to_numeric(df["집"])
df["공원"] = pd.to_numeric(df["공원"])

print(df["물가"].dtype)

# 숫자 -> 글자
# df["물가"] = df["물가"].astype(str)

# 값 없는거 평균값 채워서
df["물가"] = df["물가"].fillna(df["물가"].mean())
df["집"] = df["집"].fillna(df["집"].mean())
df["공원"] = df["공원"].fillna(df["공원"].mean())

# 물가, 집, 공원 평균내서
df["평균"] = (df["물가"] + df["집"] + df["공원"]) / 3

print(df)

# 언제 모기가 제일심했나
print(df[df["평균"] == df["평균"].max()][["날짜"]])
