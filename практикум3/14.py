n = input("Введите число: ")
while True:
    if str.isdigit(n):
        print(f'Введено целое число: {n}')
        break
    else:
        n = input('Ошибка. Попробуйте еще раз. Введите число: ')