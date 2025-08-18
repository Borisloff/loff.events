events = []
events_base = {}

def parser_load(path='events.txt'):
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            events.append(line)

    for event in events:
        try:
            if event[0] == '*':
                pass
            else:
                if event[6:10:].isdigit():
                    try:
                        events_base[event[:10:]].append({'type': 'birthday', 'name': event[11::], 'year': int(event[6:10:])})
                    except:
                        events_base[event[:10:]] = [{'type': 'birthday', 'name': event[11::], 'year': int(event[6:10:])}]

                else:
                    try:
                        events_base[event[:5:]].append({'type': 'holiday', 'name': event[6::]})
                    except:
                        events_base[event[:5:]] = [{'type': 'holiday', 'name': event[6::]}]
        except:
            return 'error'

    return events_base

def parser_dump(path='events.txt'):
    events_base = parser_load()
    with open(path, 'w', encoding='utf-8') as f:
        f.write('')
    with open(path, 'a', encoding='utf-8') as f:
        for key in events_base:
            f.write(f'{key} {events_base[key]["name"]}\n')



print(parser_load())