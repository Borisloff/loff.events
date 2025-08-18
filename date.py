from datetime import *

today = date.today()

def datenow(td=today):
    return td.strftime('%d.%m.%Y')

def datesall(td=today):
    dates = {}
    writing = {-3: '3 дня назад', -2: 'Позавчера', -1: 'Вчера', 0: 'Сегодня', 1: 'Завтра', 2: 'Послезавтра', 3: 'Через 3 дня'}
    for i in range(-3, 4):
        date = td + timedelta(days=i)
        dates[str(date.strftime('%d.%m.%Y'))] = writing[i]
    
    return dates