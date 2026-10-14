def read_rows(lines):
    if not lines:
        return []
    headline = lines[0].split(',')
    spisok = []
    for line in lines[1:]:
        line = line.split(',')
        if len(line) == 3 and all(x != '' for x in line):
            spisok.append({headline[0]: line[0], headline[1]:line[1], headline[2]:line[2]})
    return spisok

def count_types(rows):
    dict = {}
    for dict_old in rows:
        value = list(dict_old.values())[1]
        dict[value] = dict.get(value, 0) + 1
    return dict

