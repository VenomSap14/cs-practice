from tablestats import *

path = input()

with open(path, encoding="utf-8") as table:
    rows = read_rows(table.readlines())
    amount = len(rows)
    different = set()
    error_minutes = total_minutes(rows, 'ошибка')
    for row in rows:
        different.add(row['тип'])
    print(amount)
    print(len(different))
    print(error_minutes)

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(count_types(rows)))
