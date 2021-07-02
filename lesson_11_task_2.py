"""
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class ZeroDivisionError(Exception):
    def __str__(self):
        return f"you can't divide it by zero!"
class Del:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dell(self):
        if self.y == 0:
            raise ZeroDivisionError
        else:
            return self.x/self.y
d = Del(100, 0)
try:
    print(d.dell())
except ZeroDivisionError:
    print("you can't divide it by zero!")