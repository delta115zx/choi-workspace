# 개발중에 처음부터 끝까지 테스트 다?
# 중간테스트전략

######################################





f = open("C:\\Choi\\1031\\kakao_2.txt", "r", encoding="utf-8")
wordcount = {}
# 대화 내용만
# 단어수세기
for i, line in enumerate(f.readlines()):
    # if line.startswith("2019"):
    #     break
    
    msg = None
    if i > 4:
        line = line.replace("\n", "")

        if (not line.startswith("[")) and (line != ""):
            msg = line
        else:
            try:
                line = line.split("] ")
                msg = line[2]
                for ii, word in enumerate(line):
                    if ii > 1:
                        msg += " " + word
            except:
                pass
        if msg != None:
            msg = msg.strip().split(" ")
            for word in msg:
                if word in wordcount:
                    wordcount[word] += 1
                else:
                    wordcount[word] = 1

f.close()
print(wordcount)