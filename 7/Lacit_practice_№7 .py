import calendar
import sys
'''
#1
print()
print('Расположение модуля calendar',calendar.__file__)
print(dir(calendar))
print('2023 год високсный - ',calendar.isleap(2023))
print(calendar.weekday(1995,6,25))
cal= calendar.TextCalendar()
print(cal.formatyear(2023))

'''
#2
'''
a=0
for i in sys.argv:
    if a:
       print(i)
    else:
        a=1

'''
#3
'''
import dop_7
a=int(input('Первая сторона треугольника: '))
b=int(input('Первая сторона треугольника: '))
c=int(input('Первая сторона треугольника: '))
print('Площадь: ',str(dop.geron(a,b,c)))
'''
#4
'''
import datetime
day='4'
mount='12'
year='2001'
days=100000
date1=datetime.date(int(year), int(mount), int(day))
print(date1)
date2=datetime.timedelta(days=days)
print(date2)
print(date1+date2)
'''
#5
import game_7
#6
import Tkinter
