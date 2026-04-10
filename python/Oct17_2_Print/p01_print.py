# 이름이 보드마카
# 가격이 500

# 이름 자료형/주소값 확인 -> 지우시든지

# 이름출력
# 가격출력

name = "보드마카"
price = 500

# print(type(name))
# print(id(price))

# , 써서 여러개 한꺼번에 출력(띄어쓰기 해서 보여줌)
print(name, price)

print("품명은", name, "입니다. 가격은", price, "원 이구요.")

# 형식을 지정해서 출력(모든 PL들 공통)
# %s : 글자데이터 들어올 자리
print("품명은 %s입니다." % name)
# %d : 정수데이터 들어올 자리
# %06d : 무조건 6자리로, 빈자리에는 0채워서
print("가격은 %d원 이요." % price)
print("가격은 %06d원 이요." % price)

print("품명은 %s고, 가격은 %d원" % (name, price))

# %f : 실수데이터 들어올 자리
# %.3f : 소수점이하 3자리로(반올림)
length = 15.234851
print("길이는 %fcm" % length)
print("길이는 %.3fcm" % length)

isBlack = True
# %b : 논리형 데이터 들어올 자리
#       예쁘게 형식을 지정한다는 차원에서 ??
#       Python에서는 삭제됨
# print("까만색이냐? %b" % isBlack)

# %% : %
humidity = 40.345
print("습도는 %.1f%%입니다" % humidity)
