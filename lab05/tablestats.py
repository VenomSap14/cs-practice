def read_rows(lines):
    if not lines:
        return []
    headline = [x.strip() for x in lines[0].split(',')]
    spisok = []
    for line in lines[1:]:
        if not line.strip():
            continue
        line = [x.strip() for x in line.split(',')]
        if len(line) == 3:
            spisok.append({headline[0]: line[0], headline[1]:line[1], headline[2]:line[2]})
    return spisok

def count_types(rows):
    dict = {}
    for dict_old in rows:
        value = list(dict_old.values())[1]
        dict[value] = dict.get(value, 0) + 1
    return dict

def total_minutes(rows, kind):
    total = 0.0
    for dict_old in rows:
        cleaned_dict = {str(k).strip(): str(v).strip() for k, v in dict_old.items()}
        if cleaned_dict.get('тип') == str(kind).strip():
            minutes_str = cleaned_dict.get('минуты', '0')
            try:
                minutes_float = float(minutes_str.replace(',', '.'))
                total += minutes_float
            except ValueError:
                continue
    return round(total, 1)

def to_csv(counts):
    result = []
    for key in counts:
        result.append(f'{key},{counts[key]}')
    result.sort(key=lambda x: x.split(',')[0])
    if not result:
        return "тип,количество\n"
    return "тип,количество\n" + '\n'.join(result) + '\n'

