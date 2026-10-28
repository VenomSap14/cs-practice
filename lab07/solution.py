import numpy as np

def reshape_rows(values, width):
    if len(values) % width != 0:
        return []
    arr = np.array(values)
    arr = arr.reshape(int(len(values))//width, width)
    return arr.tolist()


print(reshape_rows([12, 14.5, 11, 13, 15.5, 10.5], 3))
print(reshape_rows([12, 14.5], 3))