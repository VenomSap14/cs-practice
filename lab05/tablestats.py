def read_rows(lines):
    headline = lines[0].split(',')
    spisok = []
    for line in lines[1:]:
        line.split(',')
        if len(line) >= 3:
            spisok.append(dict(headline[0]=line[0], headline[1]=line[1], headline[2]=line[2]))
    return spisok

def count_types(rows):
    dict = {}
    for value in list(rows)[1]:
        dict[value] = dict.get(value, 0) + 1
    return dict



        
