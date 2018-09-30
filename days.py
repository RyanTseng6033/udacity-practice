january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31
time = input("請輸入第一個時間:")
time = time.split("/")
day = time[2]
year = (int(time[0]))
if (year% 4== 0 and year% 100!= 0) or (year% 400== 0):
    day += 1
year = (int(time[0])-1)    
year = int(year) * 365
month = (int(time[1])-1)
if str(month) == "1":
    month = int(january)
elif str(month) == "2":
    month = int(january+february)
elif str(month) == "3":
    month = int(january+february+march)
elif str(month) == "4":
    month = int(january+february+march+april)
elif str(month) == "5":
    month = int(january+february+march+april+may)
elif str(month) == "6":
    month = int(january+february+march+april+may+june)
elif str(month) == "7":
    month = int(january+february+march+april+may+june+july)
elif str(month) == "8":
    month = int(january+february+march+april+may+june+july+august)
elif str(month) == "9":
    month = int(january+february+march+april+may+june+july+august+september)
elif str(month) == "10":
    month = int(january+february+march+april+may+june+july+august+september+october)
elif str(month) == "11":
    month = int(january+february+march+april+may+june+july+august+september+october+november)
elif str(month) == "12":
    month = int(january+february+march+april+may+june+july+august+september+october+november+december)    
totle1 = int(year) + int(month) + int(day)
time2 = input("請輸入第二個時間:")
time2 = time2.split("/")
day2 = int(time2[2])
year2 = (int(time2[0]))
if (year2% 4== 0 and year2% 100!= 0) or (year2% 400== 0):
    day2 += 1
year2 = (int(time2[0])-1)
year2 = int(year2) * 365
month2 = (int(time2[1])-1)
if str(month2) == "1":
    month2 = int(january)
elif str(month2) == "2":
    month2 = int(january+february)
elif str(month2) == "3":
    month2 = int(january+february+march)
elif str(month2) == "4":
    month2 = int(january+february+march+april)
elif str(month2) == "5":
    month2 = int(january+february+march+april+may)
elif str(month2) == "6":
    month2 = int(january+february+march+april+may+june)
elif str(month2) == "7":
    month2 = int(january+february+march+april+may+june+july)
elif str(month2) == "8":
    month2 = int(january+february+march+april+may+june+july+august)
elif str(month2) == "9":
    month2 = int(january+february+march+april+may+june+july+august+september)
elif str(month2) == "10":
    month2 = int(january+february+march+april+may+june+july+august+september+october)
elif str(month2) == "11":
    month2 = int(january+february+march+april+may+june+july+august+september+october+november)
elif str(month2) == "12":
    month2 = int(january+february+march+april+may+june+july+august+september+october+november+december)    
totle2 = int(year2) + int(month2) + int(day2)
totle = (int(totle2) - int(totle1) + 1)
print("兩個時間中間相差" + str(totle) + "天")
