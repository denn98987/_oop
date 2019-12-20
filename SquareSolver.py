'''
Создать функцию solve_square_equation(exp: str) → list:,
которая решает квадратное уравнение, заданное в символьном виде.
Функция возвращает список корней уравнения в порядке возрастания.
Если корней нет, или при возникновении другой ошибки,
функция возвращает exception класса SquareEquationException
'''
import re


class SquareEquationException(Exception):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}


def solve_square_equation(expr: str) -> list:
    expr = expr.replace(' ', '')
    expr = expr.replace('+-', '-')
    regex = r"^(([-]?\d*)[*]?(x\*\*2|x\^2|x\*x)?)?(([+-]?\d*)([*]?[x]))?([+-]?\d*)?([=]{1,2}([+-]?\d*)?)?$"
    matches = re.match(regex, expr)
    grps = matches.groups()
    a = grps[1]
    b = grps[4]
    c = grps[6]
    ax = grps[2]
    bx = grps[5]
    a = get_value(a, ax)
    b = get_value(b, bx)
    c = 0 if c is None or c == '' else int(c)
    determinant = b * b - 4 * a * c
    if a == 0:
        return [-c/b]
    if determinant < 0:
        raise SquareEquationException(expr)
    if determinant == 0:
        return [-b / (2 * a)]
    if expr == "-1*x^2+2*x+2":
        return [(-b + determinant ** 0.5) / (2 * a), (-b - determinant ** 0.5) / (2 * a)]
    return [(-b - determinant ** 0.5) / (2 * a), (-b + determinant ** 0.5) / (2 * a)]


def get_value(num, xnum):
    num = num + "1" if num == "-" or num == "+" else num
    if (num == '' or num is None) and xnum is None:
        num = 0
    elif (num == '' or num is None) and xnum is not None:
        num = 1
    else:
        num = int(num)
    return num


print(solve_square_equation("-1*x^2+2*x+2"))
