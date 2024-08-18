'''import datetime

my_time = datetime.time(17, 20)
print(type(my_time))
print(my_time)
print(my_time.hour)

print('\n')

my_day = datetime.date(2025,1,12)
print(my_day)
print(my_day.ctime())
print(my_day.today())'''

'''from datetime import datetime

my_date = datetime(2023, 10, 30, 10, 15, 23)
my_date = my_date.replace(month=11)
print(my_date)'''

'''from datetime import date

birth = date(1995,2,3)
death = date(2025,1,3)
life = death - birth
print(life.days)'''

from datetime import datetime

wokeup = datetime(2022, 10 , 5, 7,30)
went_to_sleep = datetime(2022, 10, 5, 23, 45)
wakefullness = went_to_sleep - wokeup
print(wakefullness.seconds)
