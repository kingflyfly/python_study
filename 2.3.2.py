import datetime
str = "今天是："
d = datetime.datetime.now()
day = d.weekday()
if day == 1:
    str+="星期一"
elif day == 2:
    str += "星期二"
elif day == 3:
    str += "星期三"
elif day == 4:
    str += "星期四"
elif day == 5:
    str += "星期五"
elif day == 6:
    str += "星期六"
elif day == 7:
    str += "星期天"
print(d,day)
print(str)

