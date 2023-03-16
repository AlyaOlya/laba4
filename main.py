def v1():
    try:
        first = int(input('Введите число, чтобы проверить деление на 3: '))
        second = first % 3
    except ValueError:
        print('Введено не число! ')
    else:
        if second == 0 and first != 0:
            print('Число', first, 'делится на 3!')
        elif first == 0:
            print('Введён ноль!')
        else:
            print('Число', first, 'не делится на 3!')


v1()


def v2():
    try:
        first = int(input('Введите число: '))
        second = 100 / first
    except ZeroDivisionError:
        print('Введён 0')
    except ValueError:
        print('Введено не число! ')
    else:
        print('Результат деления 100 на введённое число: ', second)


v2()

def v3():

    first= input("Ведите сюда дату в форме дд.мм.гггг: ")

    first= first.split('.')

    if int(first[0]) * int(first[1]) == int(first[2][2:4]):

        print("yes")

    else:

        print("no")




v3()


def p4()
try:
        first= input("Введите номер билета: ")
        second = list(a)
        if len(second) % 2 == 1:
            print("Это неправильный билет")

        k = int(len(second)/2)
        sum = 0
        for i in range(k):
            sum += int(second[i])
        sum2 = 0
        for i in range(k):
            sum2 += int(second[-(i+1)])
    except ValueError:
        print("Введен не номер")
    else:
        if sum == sum2:
            print("Это счастливый билет")
        else:
            print("Это не счастливый билет")

p(4)