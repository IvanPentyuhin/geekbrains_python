'''
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно сделать оптимизацию кода по памяти,
по скорости.
'''

# Проработал несколько решений и разобрал ваше!

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = []

for i in range(1, len(src)):
    a, b = src[i - 1], src[i]
    if a < b:
        result.append(b)

print(result)


result = []

for i, num in enumerate(src):
    if num > src[i - 1] and i != 0:
        result.append(num)

print(result)

#

new_list = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print(new_list)