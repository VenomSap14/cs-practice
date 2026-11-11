import numpy as np

#1

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)
print()

#2

print("Третий элемент:", hours)
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Массив в обратном порядке:", hours[::-1])
print()

#3

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print("Форма (shape):", temperatures.shape)
print("Число измерений (ndim):", temperatures.ndim)
print("Число элементов (size):", temperatures.size)
print("Значение из 2-й строки и 3-го столбца (индексы 1 и 2):", temperatures)
print("Первая строка:", temperatures)
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])

center_fragment = temperatures[0:2, 1:3]
print("Центральный фрагмент 2х2:\n", center_fragment)
print("Проверка формы фрагмента:", center_fragment.shape)
print()

#4

matrix = np.arange(1, 26).reshape(5, 5)

f1 = matrix[:3, :]
print("Первые три строки:\n", f1, "\nshape:", f1.shape)

f2 = matrix[-2:, :]
print("\nПоследние две строки:\n", f2, "\nshape:", f2.shape)

f3 = matrix[:, :2]
print("\nПервые два столбца:\n", f3, "\nshape:", f3.shape)

f4 = matrix[1:4, 2:5]
print("\nФрагмент из строк 1-3 и столбцов 2-4:\n", f4, "\nshape:", f4.shape)

f5 = matrix[-2:, -2:]
print("\nУгловой блок 2х2 в правом нижнем углу:\n", f5, "\nshape:", f5.shape)
print()

#5

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed_hours:", changed_hours)
print("исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("\nchanged_matrix:\n", changed_matrix)
print("\nисходная matrix:\n", matrix)
print()

#6

numbers = np.arange(0, 12)
table = numbers.reshape(3, 4)
transposed = table.T

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)
