# NumPy
#   실제 사용한게 np.array
#   기능 추가된 list
#   DB/OOL/... -> 다차원list? -> NumPy?
#       -> 선수과정이니까...
# Pandas(Python Data Analysis Library)
#   실제 사용하는게 pd.DataFrame
#   코딩으로 하는 MS Excel, R/Matlab
#   MS Excel놔두고?
#       -> 대용량데이터는 못하니까...
####
# pip install pandas
import pandas as pd

# list스러운거
a = pd.Series([1, 234, 534, 980])
print(a)
print(a[1])
print("-----")

# MS Excel스러운거
b = pd.DataFrame()
b["이름"] = ["새우깡", "양파링"]
b["가격"] = [3000, 4000]
print(b)
print("-----")
print(b["이름"])
print("-----") 
# Pandas가 원본데이터에 영향 안가는걸 추구
#   -> 데이터를 다루는 입장 : 안전한
#   -> 개발자 : GC...
# index : 찾는 기준
b = b.set_index(b["이름"])
print(b)
print("-----")
print(b.loc["새우깡"]) # index로 찾기
print("-----")
print(b.iloc[1]) # 번호로 찾기