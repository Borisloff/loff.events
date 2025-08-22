import os
import re
from date import yearnow
from datetime import datetime

events = []
events_base = {}

# ========== Функция для проверки строки на дату ==========
def is_real_date(text: str) -> bool:
    # сначала проверим формат: 2 цифры.2 цифры
    if not re.match(r"^\d{2}\.\d{2}$", text):
        return False

    # потом пробуем распарсить дату
    try:
        datetime.strptime(text, "%d.%m")
        return True
    except ValueError:
        return False

# ========== Функция для склонения слова "год/года/лет" ==========
def year_word(age: int) -> str:
    if 11 <= age % 100 <= 14:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'

# ========== Основная функция загрузки парсера ==========
def parser_load(path='/storage/emulated/0/Documents/Лофф.События/Sobytiya.txt'):
    global events, events_base
    events = []
    events_base = {}

    # Если файла нет — создаём пустой
    if not os.path.exists(path):
        return 'File not found'

    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                line = line.strip()
                if line:
                    events.append(line)
    except Exception:
        return 'error'

    for event in events:
        if event[0] == '*':
            continue  # служебная строка

        # День рождения: ДД.ММ.ГГГГ Имя
        if len(event) >= 11 and event[6:10].isdigit() and is_real_date(event[:5:]):
            try:
                key = event[:5]  # ДД.ММ
                year = int(event[6:10])
                age = yearnow() - year
                events_base.setdefault(key, []).append({
                    'type': 'birthday',
                    'name': event[11:],
                    'year': year,
                    'writing': year_word(age)
                })
            except:
                return 'error'

        # Праздник: ДД.MM Название
        elif len(event) >= 6 and is_real_date(event[:5:]):
            try:
                key = event[:5]
                events_base.setdefault(key, []).append({
                    'type': 'holiday',
                    'name': event[6:]
                })
            except:
                return 'error'

        else:
            return 'error'

    return events_base

# ========== Тестовый вывод для проверки ==========
if __name__ == "__main__":
    print(parser_load())
