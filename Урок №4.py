#задания №1:


a = float(input("Введите длину первой стороны прямоугольника: "))
b = float(input("Введите длину второй стороны прямоугольника: "))

area = a * b
perimeter = 2 * (a + b)

print(f"Площадь прямоугольника: {area}")
print(f"Периметр прямоугольника: {perimeter}")

#задания №2:


num = input("Введите пятизначное число: ")
tens = int(num[3])
ones = int(num[4])
hundreds = int(num[2])
tens_of_thousands = int(num[0])
thousands = int(num[1])
result = (tens ** ones * hundreds) / (tens_of_thousands - thousands)


print(f"Результат: {result}")