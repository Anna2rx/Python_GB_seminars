print("Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.")
a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите кол-во элементов: "))
p = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*p)
print("-----------------------------------------")

print("Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)")
a = [int(input(f"Введите {i + 1}-й элемент: ")) for i in range(int(input("Введите количество элементов списка: ")))]
b1 = int(input("Введите нижнюю границу диапазона: "))
b2 = int(input("Введите верхнюю границу диапазона: "))
indexes = [i for i in range(len(a)) if b1 <= a[i] <= b2]
print(indexes)