#Задание №1


n = int(input("Введите количество чисел: "))
count = 0
for i in range(n):
    num = int(input("Введите число: "))
    if num == 0:
        count += 1
print("Количество нулей:", count)

#Задание №2

x = int(input("Введите натуральное число: "))
count = 0
i = 1
while i * i <= x:
    if x % i:
        pass
    elif i * i == x:
        count += 1
    else:
        count += 2
    i += 1
print("Количество делителей:", count)


#Задание №3


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end = ' ')


