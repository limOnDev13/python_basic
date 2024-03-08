from typing import Any


class Matrix:

    def __init__(self, rows: int, cols: int, matrix: list[list[int | float]]):
        self.rows: int = rows
        self.cols: int = cols
        self.matrix: list[list[int | float]] = matrix

    def __str__(self):
        """
        Метод красиво выводит матрицу в консоль.
        :return: Ничего
        """
        return '\n'.join(['\t'.join([str(col) for col in row]) for row in self.matrix])

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('Размеры матриц не совпадают!')
            else:
                return Matrix(self.rows, self.cols,
                              [[self_col + other_col
                               for self_col, other_col in zip(self_row, other_row)]
                               for self_row, other_row in zip(self.matrix, other.matrix)])
        elif isinstance(other, int | float):
            return Matrix(self.rows, self.cols,
                          [[col + other for col in row]
                           for row in self.matrix])
        raise TypeError('Матрицы можно складывать с другими матрицами тех же размеров или с числом')

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('Размеры матриц не совпадают!')
            else:
                return Matrix(self.rows, self.cols,
                              [[self_col - other_col
                               for self_col, other_col in zip(self_row, other_row)]
                               for self_row, other_row in zip(self.matrix, other.matrix)])
        elif isinstance(other, int | float):
            return Matrix(self.rows, self.cols,
                          [[col - other for col in row]
                           for row in self.matrix])
        raise TypeError('Матрицы можно складывать с другими матрицами тех же размеров или с числом')

    def transpose(self) -> Any:
        """
        Метод транспонирует матрицу.
        :return: Транспонированную матрицу.
        """
        return Matrix(
            rows=self.cols,
            cols=self.rows,
            matrix=[[self.matrix[row][col] for row in range(self.rows)]
                    for col in range(self.cols)]
        )

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError('Количество столбцов первой матрицы не совпадает с количеством строк второй!')
            else:
                return Matrix(self.rows, self.cols,
                              [[sum([col * row for col, row in zip(self_i_row,
                                                                   other_i_col)])
                                for other_i_col in other.transpose().matrix]
                               for self_i_row in self.matrix
                               ])
        elif isinstance(other, int | float):
            return Matrix(self.rows, self.cols,
                          [[col * other for col in row]
                           for row in self.matrix])
        raise TypeError('Матрицы можно складывать с другими матрицами тех же размеров или с числом')



# Примеры работы с классом (примеры из задания изменены и внесение списка чисел происходит при
# инициализации:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])

m2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1 + m2)

print("Вычитание матриц:")
print(m1 - m2)

m3 = Matrix(3, 2, [[1, 2], [3, 4], [5, 6]])

print("Умножение матриц:")
print(m1 * m3)

print("Транспонирование матрицы 1:")
print(m1.transpose())
