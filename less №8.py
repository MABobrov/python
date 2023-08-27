"""Задание 1"""

def reverse_array():
    N = int(input("Введите число N: "))
    arr = []
    for _ in range(N):
        arr.append(int(input()))

    # переворачиваем массив
    arr.reverse()
    for num in arr:
        print(num)




"""Задание 2"""


def alternate_array():
    N = int(input("Введите число N: "))
    arr = list(map(int, input().split()))

    result = [0] * N
    result[::2] = arr[N//2:]
    result[1::2] = arr[:N//2]

    for num in result:
        print(num, end=' ')





"""Задание 3"""

def minimum_boats():
    m = int(input("Максимальная масса, которую может выдержать одна лодка: "))
    n = int(input("Количество рыбаков: "))
    weights = [int(input()) for _ in range(n)]
    weights.sort()
    count = 0
    i = 0
    j = n - 1
    while i <= j:
        if weights[i] + weights[j] <= m:
            i += 1
        j -= 1
        count += 1
    print(count)


reverse_array()
alternate_array()
minimum_boats()