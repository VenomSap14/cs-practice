import numpy as np

def reshape_rows(values, width):
    if len(values) == 0 or width == 0:
        return []
    if len(values) % width != 0:
        return []
    arr = np.array(values)
    arr = arr.reshape(int(len(values))//width, width)
    return arr.tolist()

def block(matrix, rows, columns):
    matrix = np.array(matrix)
    return matrix[np.ix_(rows, columns)].tolist()

def column_means(matrix):
    matrix = np.array(matrix)
    res = np.round(matrix.mean(axis=0), 6)
    return res.tolist()

def column_range(matrix, column):
    matrix = np.array(matrix)
    col_matrix = matrix[:, column]
    return round(col_matrix.max() - col_matrix.min(), 6)

