'''
Разработать класс Polynom, объекты которого представляют собой полином.
При создании объекта данного класса указываются коэффициенты полинома, начиная с коэффициента при старшей степени.
пример создания полинома A = Polynom(-1, 0, 3, 0).
При создании полинома, указываются все коэеффициенты, даже равные 0.
К объектам типа Polynom должны быть применимы операции сложения, вычитания, умножения, как на другие полиномы,
так и на обычные числа и сравнения двух полиномов между собой.
Кроме этого необходимо уметь выводить полином на экран при помощи команды print()
при выводе полинома на экран, степени с коэффициентом раным 0, не выводить, коэффициент и степень равные 1 не выводить.
Полином должен выводиться на экран в виде 3x^2-x+2, или -5x^2+x^4-2x, x+2
Также необходимо считать значение полинома в указанной точке.
'''


def adding(coefs, other):
    sub = len(coefs) - len(other)
    res = [*coefs[0:sub]]
    for x in range(sub, len(coefs)):
        res.append(coefs[x] + other[x - sub])
    return res


def negat(other):
    res = []
    for x in other:
        res.append(-1 * x)
    return res


def get_nom(n):
    if n == 0:
        return ""
    elif n == 1:
        return "x"
    else:
        return "x^"+str(n)


class Polynom:
    coefs = []

    def __init__(self, *params):
        self.coefs = [x for x in params]

    def __len__(self):
        return len(self.coefs)

    def __add__(self, other):
        if type(other) != Polynom:
            return Polynom(*adding(*self.coefs, [other]))
        if len(self.coefs) > len(other):
            return Polynom(*adding(self.coefs, other))
        else:
            return Polynom(*adding(other, self.coefs))

    def __sub__(self, other):
        if len(self.coefs) > len(other):
            return Polynom(*adding(self.coefs, negat(other)))
        else:
            return Polynom(*adding(other, negat(self.coefs)))

    def __mul__(self, other):
        if type(other) != Polynom:
            return Polynom(*[x*other for x in self.coefs])
        res = Polynom()
        for x in range(len(self)):
            temp_list = [0]*(len(self) + len(other) - 1)
            for y in range(len(other)):
                temp_list[x + y] = self[x] * other[y]
            temp = Polynom(*temp_list)
            res += temp
        return res

    def __eq__(self, other):
        if self.coefs == other:
            return True
        return False

    def __str__(self):
        res = ""
        length = len(self.coefs)
        for x in range(len(self.coefs)):
            if self.coefs[x] == 0:
                continue
            res += "+"
            if self.coefs[x] == 1 and length - x - 1 > 0:
                res += get_nom(length-x-1)
            elif self.coefs[x] == -1 and length - x - 1 > 0:
                res += "-"+get_nom(length-x-1)
            elif abs(self.coefs[x]) == 1 and length - x == -1:
                res += str(self.coefs[x]) + get_nom(length-x-1)
            else:
                res += str(self.coefs[x]) + get_nom(length-x-1)
        res = res.replace("++", "+")
        res = res.replace("+-", "-")
        if res[0] == "+":
            res = res[1:]
        if res[-1] == "+":
            res = res[:-1]
        return res

    def __iter__(self):
        for x in self.coefs:
            yield x

    def __getitem__(self, item):
        return self.coefs[item]

    def __call__(self, x):
        res = 0
        for i in range(len(self)):
            if i == 0:
                res = res + self[len(self) - 1]
            else:
                res = res + self[len(self) - 1 - i] * (x ** i)
        return res

import unittest


class TestHomework(unittest.TestCase):
    def test_add_one_num(self):
        first = Polynom([0, 1, 2])
        second = 1
        res = first + second
        self.assertEqual(res, Polynom(*[0, 1, 3]))

    def test_adding(self):
        first = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        second = [5, 4, 3, 2, 1]
        res = adding(first, second)
        self.assertEqual(res, [0, 1, 2, 3, 4, 10, 10, 10, 10, 10])

    def test_adding_same_length(self):
        first = [0, 1, 2, 3, 4]
        second = [5, 4, 3, 2, 1]
        res = adding(first, second)
        self.assertEqual(res, [5, 5, 5, 5, 5])

    def test_otr(self):
        first = [0, 1, 2, 3, 4]
        res = negat(first)
        self.assertEqual(res, [0, -1, -2, -3, -4])

    def test_sub_same_length(self):
        first = [0, 1, 2, 3, 4]
        second = [5, 4, 3, 2, 1]
        res = adding(first, negat(second))
        self.assertEqual(res, [-5, -3, -1, 1, 3])

    def test_sub(self):
        first = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        second = [5, 4, 3, 2, 1]
        res = adding(first, negat(second))
        self.assertEqual(res, [0, 1, 2, 3, 4, 0, 2, 4, 6, 8])

    A = Polynom(1, 2, 3)
    B = Polynom(3, 2, 1)

    def test_equlas(self):
        self.assertEqual(self.A, self.A)

    def test_not_equal(self):
        self.assertNotEqual(self.A, self.B)

    def test_add(self):
        res = self.A + self.B
        asss = Polynom(4, 4, 4)
        self.assertEqual(res, asss)

    def test_mul(self):
        res = self.A * 3
        self.assertEqual(res, Polynom(3, 6, 9))

    def test_mul_two_polinoms(self):
        A = Polynom(*[1, 1])
        B = Polynom(*[1, 2])
        res = A * B
        self.assertEqual(res, Polynom(1, 3, 2))

    def test_str(self):
        res = str(Polynom(10, -1, -1))
        self.assertEqual(res, "10x^2-x-1")

    def test_call(self):
        res = Polynom(1)(1)
        self.assertEqual(res, 1)

    def test_call_2(self):
        A = Polynom(2.3, 1.05, 1.64)
        res = A(1.36)
        self.assertEqual(res, 7.32208)

    def test_call_3(self):
        A = Polynom(1, -1.36)
        res = A(1.36)
        self.assertEqual(res, 0.0)

if __name__ == '__main__':
    unittest.main()
