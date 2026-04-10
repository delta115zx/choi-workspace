# 분석/AI결과 시각화
# ... -> 결과를 파일로 저장 -> Excel
# ... -> 결과를 JSON으로 응답하는 Back-End -> canvasjs같은 JS라이브러리
# Python 시각화 lib : Matplotlib
# pip install matplotlib
from turtle import color
from matplotlib.lines import lineStyles
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Matplotlib 기본 폰트에 한글 없음 -> 한글되는 폰트로 바꾸자(그나마도 다 되는건 아닌)
# C:\Windows\Fonts에 가서 cmd -> dir로 폰트파일명 확인
fontFile = "C:/Windows/Fonts/malgun.ttf"  # 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()  # 폰트명
plt.rc("font", family=fontName)  # Matplotlib 기본폰트 바꾸기
plt.rcParams["axes.unicode_minus"] = False  # -안깨지게

# matplotlib이 np.array를 대상으로
xData = np.array([10, 20, 30, 40, 50])
yData = [22, 45, 2, 10, 3]  # 쌩list -> np.array로 바꿔서

# 기본
# plt.plot(yData) # plt에 이래저래 세팅
# plt.show() # 나오게

# x, y
# plt.plot(xData, yData)
# plt.show()

# 축
# plt.plot(xData, yData)
# plt.xlabel("엑스축")
# plt.ylabel("y-axis")
# plt.axis([0, 300, -10, 50])  # x최소, x최대, y최소, y최대
# plt.show()

# 제목
# d = {"fontsize": 20, "fontweight": 900, "color": "#ff0000"}
# plt.plot(xData, yData)
# plt.title("제목")
# plt.title("제목2", loc="left")
# plt.title("제목3", loc="right", fontdict=d)
# plt.show()

# 선(간단)
# plt.plot(xData, yData, "c:*")
# plt.show()

# 선(정식)
# plt.plot(xData, yData, color="k", linestyle="--", marker="X", linewidth=5)
# plt.show()

# 격자
plt.plot(xData, yData)
plt.grid(axis="both", color="salmon", linestyle="--")
plt.show()
