# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# def sum(a,b)
num_a = int(input('введите число А: '))
num_b = int(input('введите число B: '))

def sum (a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum(a - 1, b + 1)
print(f'{num_a} + {num_b} = {sum(num_a, num_b)}')
