# 반복문 제어
#   break : 반복문 종료
#   continue : 턴 종료(강제 반복)
for i in range(1, 100, 3):
    if i % 10 == 0:
        break
    print(i)
print("--------")

for i in range(1, 100, 3):
    if i % 10 == 0:
        continue
    print(i)
print("--------")

# == True는 생략가능
# == False는 not xx로
iBreak = False
for i in range(3):
    if iBreak:
        break
    for j in range(3):
        if iBreak:
            break
        for k in range(3):
            if k == 1:
                iBreak = True
                break
            print(i, j, k)

print("--------")

# while문 구조상
#   작업내용 밑에
#   조건식이 위에
#   -> 조건식 쓰기가 애매

# 멘트 입력 -> 출력
# 나가라고 입력하면 종료
while True:
    a = input("뭐: ")
    print(a)
    if a == "나가":
        break
print("--------")