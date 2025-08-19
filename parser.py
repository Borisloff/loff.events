import os
from date import yearnow

events = []
events_base = {}

# ===== Функция для склонения слова "год/года/лет" =====
def year_word(age: int) -> str:
    if 11 <= age % 100 <= 14:
        return 'лет'
    elif age % 10 == 1:
        return 'год'
    elif 2 <= age % 10 <= 4:
        return 'года'
    else:
        return 'лет'

# ===== Основная функция загрузки парсера =====
def parser_load(path='events.txt'):
    global events, events_base
    events = []
    events_base = {}

    # Если файла нет — создаём пустой
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            pass  # просто создаём пустой файл
        print(f'Файл "{path}" не найден. Создан пустой файл.')

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
        if len(event) >= 11 and event[6:10].isdigit():
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
        elif len(event) >= 6:
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

# ===== Тестовый вывод для проверки =====
if __name__ == "__main__":
    print(parser_load())