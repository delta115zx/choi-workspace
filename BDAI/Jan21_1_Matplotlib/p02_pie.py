import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

# 파이차트 : 점유율
#   파이차트는 큰 순서로 보여주는게 기본, 정렬기능은 없음
data = [28, 1, 10]
label = ["901", "903", "902"]
e = [0, 0, 0.3]
w = {"width": 0.7, "edgecolor": "black", "linewidth": 3}
plt.pie(data, labels=label, autopct="%.1f%%", startangle=45, explode=e, wedgeprops=w)
plt.show()
