from datetime import datetime,date,time,timedelta
#date
dateobject = date(2003,12,4)
print(dateobject)
print(dateobject.year)
print(dateobject.month)
print(dateobject.day)

#date today
print(date.today())

#date arithmetic
date1 = date(2003,5,15)
date2 = date(2026,3,30)

datesum = date2-date1
print(datesum.days)

#time arithmetc
time1 = time(9,39,45,1000)
time2 = time(4,39,45,1000)

timesub = timedelta(hours = time1.hour-time2.hour,)#.... minutes,seconds,microseconds
print(f"deltatime:{timesub}")

#datetime
print(datetime.now())
print(datetime(2002,4,5,3,10,45,1000))

#strftime
currentdate = datetime.now()
formatteddate = currentdate.strftime("%Y-%m-%d %H:%M:%S")
print(formatteddate)

#strptime
manualdate= datetime.strptime("2002-05-5 12:57:10", "%Y-%m-%d %H:%M:%S")
print(manualdate)
