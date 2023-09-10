import sys
import math
from math import pi
def calculator() :
    print('Enter operation symbol : ')
    operationsymbol = input()
    if operationsymbol == 'pi':  # Число пи
        return pi

    print('Введите x: ')
    x = int(input())
    fac = 1
    if operationsymbol == '!':
        while x > 1:
            fac *= x
            x -= 1
        return x
    print('Введите y: ')
    y = int(input())
    if operationsymbol == '+':
        print(x + y)

    if operationsymbol == '/':
        return x/y
    if operationsymbol == '-':
        return x - y
    if operationsymbol == 'sqrt':
        return pow(x, x)

    if operationsymbol == '*':
        return x * y


    print('Ответ : ' + str(calculator()))
print(calculator())