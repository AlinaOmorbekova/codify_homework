
#Написать программу с помощью которой пользователь, по выбору, может посмотреть
# - текущее число
# - месяц
# - год
# - время
# - полную дату и время в формате '%m/%d/%Y %H:%M:%S'
import datetime

def date_time(see_date):
    current_date = datetime.datetime.today()
    if see_date == 1:
        print('Текущее число: ', datetime.date.today())
    elif see_date == 2:
        print('Текущий месяц: ',current_date.month)    
    elif see_date == 3:
        print('Текущий год: ', current_date.year)
    elif see_date == 4:
        print('Текущее время: ', current_date.time())
    elif see_date == 5:
        print('Полная дата и время: ', current_date.strftime("%m/%d/%Y %H:%M:%S"))   
                     
see_date = int(input('''
    Выберите функцию:
    1. Посмотреть текущее число
    2. Посмотреть месяц
    3. Посмотреть год
    4. Посмотреть время
    5. Посмотреть полную дату и время в формате '%m/%d/%Y %H:%M:%S
     '''))        
date_time(see_date)
