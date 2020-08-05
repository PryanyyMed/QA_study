#1. Принимаю от пользователя дату
#2. Составляю расписание раз в 2 дня (через день)
#3. На 30 дней ДД ММ ГГ и день недели
#4. Если это воскресенье, то перенести на понеделтник и опять через день

import datetime
#прошу у пользователся дату
date_entry = input("Введите дату в формате ДД, ММ, ГГГГ ")

#перевожу в формат даты ДД ММ ГГГГ - если ввести формат по-другому, то программа не запустится
dt = datetime.datetime.strptime(date_entry, "%d, %m, %Y")

#вывод списка по дням
#скачать pip DateTimeRange (https://pypi.org/project/DateTimeRange/#get-iterator)
from datetimerange import DateTimeRange
# date_End - финальная дата через 30 дней
date_End = datetime.timedelta(days=30)
time_range = DateTimeRange(dt, dt + date_End)
print ("Расписание на месяц: ")
#список выводится через день (days=2)
for value in time_range.range(datetime.timedelta(days=2)):
#проверка на то, что будут выводиться дни с пн до сб
    if value.weekday() in range(0,6):
        print(value.strftime ("%A, %d %B, %Y"))
