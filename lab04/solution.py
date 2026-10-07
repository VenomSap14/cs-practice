def winner(names, scores):
    max = float('-inf')
    for i in range(len(scores)):
        if scores[i] > max:
            max = scores[i]
            max_i = i
    return names[max_i]

def average(scores):
    if len(scores) > 0:
        return round(sum(scores)/len(scores),2)
    else:
        return 0

def ranking(names, scores):
    spisok = []
    for i in range(len(names)):
        spisok.append([names[i], scores[i]])
    spisok.sort(key=lambda x: -x[1])
    return [x[0] for x in spisok]

def above_average(names, scores):
    avg = average(scores)
    spisok = []
    for i in range(len(names)):
        spisok.append([names[i], scores[i]])
    return [x[0] for x in spisok if x[1] > average]

