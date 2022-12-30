# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи



def Fibonacci(n):
    fList = []
    a, b = 1, 1
    for i in range(n):
        fList.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fList.insert(0, a)
        a, b = b, a - b
    return fList

number = int(input('Введите число: '))
fList = Fibonacci(number)
print(fList)



