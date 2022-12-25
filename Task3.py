# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

number = int(input('Введите размер списка: '))
my_list = []
for i in range(number):
    element = uniform(0, 9)
    my_list.append(round(element, 2))

min = my_list[0]
max = 0

for i in range(len(my_list)):
    fraction = float(my_list[i] - int(my_list[i]))
    if max < fraction:
        max = fraction
    if min > fraction:
        min = fraction

print(f'{my_list}\n Максимальное значение дробной части - {round(max, 2)},\n Минимальное значение дробной части - {round(min, 2)},\n Разница между ними - {round(max - min, 2)}')


