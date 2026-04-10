# 자건거 바퀴둘레 : 100
# 앞 기어 톱니수 : 4
# 뒷 기어 톱니수 : 2
# 발 구른 횟수 : 3
# --------------
# 총 이동거리는 :

a = float(input("자전거 바퀴둘레 : "))
b = int(input("앞 기어 톱니수 : "))
c = int(input("뒷 기어 톱니수 : "))
d = float(input("발 구른 횟수 : "))
result = (d * b / c) * a
print("--------------")
print("총 이동거리는: %.1fcm" % result)


