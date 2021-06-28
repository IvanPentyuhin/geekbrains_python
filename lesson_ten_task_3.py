"""
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv____truediv__()).
Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
округление до целого числа деления клеток соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
"""



class Cell:
    def __init__(self, num: int):
        self.number_of_cells = num

    def __add__(self, other):
        return f'Операция объединения двух клеток. Результат: {self.number_of_cells + other.number_of_cells}'

    def __sub__(self, other):
        if self.number_of_cells - other.number_of_cells != 0:
            a = self.number_of_cells - other.number_of_cells
            b = (a)
            return f'Вычитание клеток. Результат:{b}'
        else:
            return f'Клетка больше не существует.'

    def __mul__(self, other):
        return f'Умножение клеток. Результат: {self.number_of_cells * other.number_of_cells}'

    def __truediv__(self, other):
        return f'Деление клеток. Результат: {self.number_of_cells // other.number_of_cells}'

    def make_order(self, row):
        cel = ''
        for i in range(int(self.number_of_cells / row)):
            cel += '*' * row + '\n'
        cel += '*' * (self.number_of_cells % row) + '\n'
        return cel


cell1 = Cell(15)
cell2 = Cell(5)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(10))