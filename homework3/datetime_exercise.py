from datetime import date, timedelta, datetime

print('Сейчас, вчера и 30 дней назад:')

right_now = date.today()
print(right_now)

one_day = timedelta(days=1)
yesterday_123 = right_now - one_day
print(yesterday_123)

one_mounth = timedelta(days=30)
one_mounth_ago = right_now - one_mounth
print(one_mounth_ago)
print()
print('Преобразование строки в дату:')
str_value = "01/01/25 12:10:03.234567"
date_value = datetime.strptime(str_value, '%m/%d/%y %H:%M:%S.%f')
print(date_value)