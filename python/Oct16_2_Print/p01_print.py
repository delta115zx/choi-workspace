# 왜x
# 언제 : 중간테스트 값 찍어보는 용도

# 콘솔창에 ㅋ출력
print("ㅋ")
print("ㅎ", end="") # 출력하고나서 줄 안바꿈
print("ㅇ")

# 콘솔창에 /출력
# 콘솔창에 -출력
# 콘솔창에 \출력
print("/")
print("-")
# print("\")

# Python만 해당x
# 모든 PL들의 공통사항
# \n : new line - 줄만 바꾸기
# \r : carrage return - 커서를 맨 앞으로
# 진짜 엔터하려면 : \r\n해야(Python은 고급언어라서 \n만 해도 봐줌)
# \t : tab - tab키
# \b : backspace(1byte 지우기)
#   1글자를 표현하는데 1byte를 쓰는 언어는 정상작동
#   Python은 1글자 표현에 2bytes이상 써서 정상작동 안됨
# \\ : \
# \" : "
print("ㅋ\nㅎ")
print("ㄱㄱㄱ\rㄴ")
print("ㅠ\tㅜ")
print("ㅠㅠ\tㅜ")
print("ㅡㅡ\b")
print("\\")
print("\"")