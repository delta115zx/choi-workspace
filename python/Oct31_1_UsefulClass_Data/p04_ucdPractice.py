# 개발중에 처음부터 끝까지 테스트 다?
# 중간테스트전략

######################################





f = open("C:\\Choi\\1031\\kakao.txt", "r", encoding="utf-8")
# 대화 내용만
# 단어수세기
data = []
for line in f.readlines():
    line = line.replace("\n", "")
    line = line.split("]")
    if len(line) < 3:
        continue
    msg = line[2]
    data.append(line[2])
    print(msg)
print("===============")
print(data)

f.close

    