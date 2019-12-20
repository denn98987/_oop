'''
Разработать функцию, calculator_math_express(expr: str)→ float:
которая принимает в себя строку, представляющую собой математическое выражение,
и возвращает результат его вычисления. В математическом выражении могут встречаться числа,
круглые скобки и знаки операций вида +, -, *, /. Если математическое выражение некорректное,
например неправильный баланс скобок, или происходит некорректная операция, например деление на 0,
то функция возвращает exception MathExpressionException
Операция унарный минус в математчиеском выражении отсутствует
'''
class MathExpressionException(Exception):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}


def calculator_math_express(expr: str)-> float:
    try:
        return eval(expr)
    except:
        raise MathExpressionException(expr)
