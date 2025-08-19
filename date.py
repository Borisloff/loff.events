from datetime import *

today = date.today()

def datenow(td=today):
    return td.strftime('%d.%m')


def datesall(td=None):
    if td is None:
        td = date.today()

    # Офсет в днях по порядку: вчера, сегодня, завтра, через неделю
    offsets = [0, 1, -1, 7]

    # Список дат в формате 'ДД.ММ'
    dates_list = [(td + timedelta(days=offset)).strftime('%d.%m') for offset in offsets]

    return dates_list

def yearnow(td=today):
    return int(td.strftime('%Y'))

print(datesall())