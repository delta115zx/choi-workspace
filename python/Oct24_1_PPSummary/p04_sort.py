from operator import le


def bubbleSort(l):
    for turn in range(len(l) - 1):  # 0 ~ 3
        for i in range(len(l) - 1 - turn):  # 0 ~ 3
            if l[i] > l[i + 1]:  # 0턴 : 01 12 23 34, 1턴 01 12 23 , ....
                l[i], l[i + 1] = l[i + 1], l[i]


def selectionSort(l):
    for turn in range(0, len(l) - 1):  # 0 ~ 3까지
        min = l[turn]  # 일단은 turn번이 최소값이라고 치고
        minIndex = turn  # 최소값이 turn번에 있다고 치고
        for i in range(turn + 1, len(l)):  # turn+1 ~ 4 까지
            if min > l[i]:  # 최소값보다 i번째 있는게 작으면
                min = l[i]  # 그게 최소값
                minIndex = i  # 최소값은 i번째에 있는거
        l[turn], l[minIndex] = l[minIndex], l[turn] # turn번이랑 최소값있는 위치 자리 바꾸기


##############################
# list를 넣으면 오름차순 정렬해주는 함수

l = [765, 211, 21, 1786, 2]

# 그거 불러서 정렬
# bubbleSort(l)
# print(l)

selectionSort(l)
print(l)
