from math import *

while True:
    n = int(input("Введите число: "))
    if n < 0:
        print("Число не является полным квадратом ")
        continue
    r = int(sqrt(n))

    if r**2 == n:
        print("Число является полным квадратом")
        break
    else:
        print("Число не является полным квадратом ")