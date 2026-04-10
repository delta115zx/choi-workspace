import pandas as pd
import numpy as np

# Python list
a = pd.DataFrame()
a["이름"] = ["홍길동", "김길동"]
a["나이"] = [20, 30]
print(a)
print("-----")

# np.array
b = pd.DataFrame()
b["이름"] = np.array(["홍길동", "김길동"])
b["나이"] = np.array([20, 30])
print(b)
print("-----")

# 2차원 list/np.array
c = [["홍길동", 20], ["김길동", 30]]
c = pd.DataFrame(c, columns=["이름", "나이"])
print(c)
print("-----")

# dict + list
d = {"이름": ["홍길동", "김길동"], "나이": [20, 30]}
d = pd.DataFrame(d)
print(d)
print("-----")

# list + dict
e = [{"이름": "홍길동", "나이": 20}, {"이름": "김길동", "나이": 30}]
e = pd.DataFrame(e)
print(e)
