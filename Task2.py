# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list1 = [2, 3, 4, 5, 6]
my_list2 = []
result = 1

for i in range(len(my_list1)):
    index = len(my_list1) - 1
    if i < len(my_list1) / 2:
        result = my_list1[i] * my_list1[index - i]
        my_list2.append(result)
    index-=1

print(f'{my_list1} => {my_list2}')


