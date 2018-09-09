def charge(km):
    if km > 0 and km <= 20:
        return "不用收費"
    elif km > 20 and km <= 200:
        km -= 20
        return str(km * 1.2) + "元"
    elif km > 200:
        km -= 20
        return str(km * 0.8 + 1.2 * 200) + "元"
    else:
        return "請重新輸入"
print(charge(int(input("請輸入公里數:"))))


