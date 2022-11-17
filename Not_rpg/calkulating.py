import math

import itertools


message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    result = sqrt(number)
    return result


def calc(your_number):
    if your_number <= 0:
        return
    print("Мы вычислили квадратный корень из введённого вами числа. "
          f"Это будет: {calculate_square_root(your_number)}")


calc(25.5)
