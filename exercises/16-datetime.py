from datetime import datetime
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38}

t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5

from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)



#Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print("now gets:",f'{now.day}/{now.month}/{now.year} {now.hour}:{now.minute}')

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print("now strftime:",now.strftime("%m/%d/%Y, %H:%M:%S"))

#Today is 5 December, 2019. Change this time string to time.
date_string = "12 February, 1978"
print("strptime:", datetime.strptime(date_string, "%d %B, %Y"))

#Calculate the time difference between now and new year.
new_year = date(now.year+1, 1 , 1)
print(new_year-now.date())

#Calculate the time difference between 1 January 1970 and now.
from datetime import timedelta
new_year = date(1978, 2 , 12)
timedelta()
print("diff:", now.date()-new_year)



#Think, what can you use the datetime module for? Examples:
#Time series analysis
#To get a timestamp of any activities in an application
#Adding posts on a blog