x1 = int(input("請輸入A的x1:"))
x2 = int(input("請輸入A的x2:"))
x3 = int(input("請輸入B的x1:"))
x4 = int(input("請輸入B的x2:"))
x5 = int(input("請輸入C的x1:"))
x6 = int(input("請輸入C的x2:"))
if int(x3) - int(x2) <= 0 and int(x5) - int(x4) <= 0:
    answer = int(x6)  - int(x1)
    print(answer)
elif int(x3) - int(x2) <= 0 and int(x5) - int(x4) >= 0:
    answer = int(x4) - int(x1) + int(x6) - int(x5)
    print(answer)
elif int(x3) - int(x2) >= 0 and int(x5) - int(x4) <= 0:
    answer = int(x2) - int(x1) + int(x6) - int(x3)
    print(answer)
else:
    answer = int(x2) - int(x1) + int(x4) - int(x3) + int(x6) - int(x5)
    print(answer)
