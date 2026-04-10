import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

# 꺾은선그래프
#   xData가 어떻게 변할때, yData가 어떻게 변하나 추이
#   -> yData는 당연히 숫자, xData도 숫자여야

yData = [12, 10, 5, 22, 8]
xData = [10, 20, 30, 40, 50]

# 눈금
# plt.plot(xData, yData)
# plt.xticks(xData, ["십", "이십", "삼십", "사십", "오십"])
# # plt.yticks(yData, ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"]) # 12 -> ㄱ, 10 -> ㄴ, ...
# plt.yticks(np.arange(0, 23, 5), ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"])  # 0 -> ㄱ, 5 -> ㄴ, ...
# plt.tick_params("x", direction="inout", length=20, pad=15)
# plt.tick_params("y", color="#ff0000", labelcolor="#00ff00", labelsize=20)
# plt.show()

# 선 여러개
# yData2 = [10, 50, 22, 4, 6]
# plt.plot(xData, yData)
# plt.plot(xData, yData2, "r-.")
# plt.legend(["와이데이터", "222"])
# plt.show()

# 선 여러개2
yData3 = [100000, 50000, 900000, 203023, 800303]

_, sub1Conf = plt.subplots()
p1 = sub1Conf.plot(xData, yData)
sub1Conf.set_xlabel("엑스")
sub1Conf.set_ylabel("와이")

sub2Conf = sub1Conf.twinx()
p2 = sub2Conf.plot(xData, yData3, "r")
sub2Conf.set_ylabel("와이3")

sub1Conf.legend(p1+p2, ["와이이", "와이이333"])

plt.show()
