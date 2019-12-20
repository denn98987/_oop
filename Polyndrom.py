'''
Создать функцию is_polyndrom(num: int)→ int:
которая проверяет, является ли строчное представление
заданного числа палиндромом в какой нибудь системе счисления.
На вход подается число, функция возвращает основание системы
счисления, в которой число является палиндромом.
В качестве основания системы счисления сможет выступать
любое число от 2 до 36. Если таких систем счисления
существует несколько, то вернуть наименьшее основание.
Если такой системы счисления не существует,
то функция должна вернуть 0.
'''


def is_polyndrom(n: int) -> int:
    for x in range(2, 37):
        strN = str(convert_base(n, to_base=x))
        if strN == strN[::-1]:
            return x
    return 0


def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]

print(is_polyndrom(4))