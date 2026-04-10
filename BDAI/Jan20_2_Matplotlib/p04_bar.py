import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

# 막대그래프 : 단순히 항목간 크기비교
#   -> xData는 숫자가 아니어도 되는데...
#   -> xData를 숫자로 주는게 편할
yData = [10, 12, 5, 22, 8]
xLabel = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"]
xData = np.arange(len(xLabel))

# 기본
# plt.bar(xData, yData)
# plt.show()

# 기본2
# plt.bar(xData, yData)
# plt.xticks(xData, xLabel)
# plt.show()

# 디자인
# plt.bar(xData, yData, color="#FF0000", width=0.3, # x값
#          edgecolor="#0000FF", linewidth=5) # px
# colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF"]
# plt.bar(xData, yData, color=colors, width=0.3, edgecolor="#0000FF", linewidth=5)
# plt.show()

# y값 여러개(옆에) - 자체 기능은 없음
# yData2 = [10, 55, 3 ,20, 15]
# plt.bar(xData, yData, width=0.3, align="edge") # xData=[0 1 2 3 4]
# plt.bar(xData-0.3, yData2, width=0.3, align="edge") # xData=[-0.3 0.7 1.7 2.7 3.7]
# plt.show()

# y값 여러개(위로)
yData2 = [12, 4, 3, 6, 11]
plt.bar(xData, yData)
plt.bar(xData, yData2, bottom=yData)
plt.show()