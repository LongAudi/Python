import calendar

nam1 = int(input("Mời bạn nhập vào năm bất kì 1: "))
# nam2 = int(input("Mời bạn nhập vào năm bất kì 2: "))
for month in range(1, 13):
    mycal = calendar.monthcalendar(nam1,month) 
    week1 = mycal[1]
    week2 = mycal[2]
    if week1[calendar.SUNDAY] != 0:
        auditday = week1[calendar.SUNDAY]
    else:
        auditday = week2[calendar.SUNDAY]
    print("%10s %2d" % (calendar.month_name[month], auditday))