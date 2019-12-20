'''
Разработать класс Stack, объект которого представляет собой типизированный стек.
При создании объекта класса указывается, объекты какого именного класса должны в нем хранится,
после этого, в стек можно добавлять либо объекты указанного класса, либо производные от него.
При добавлении объектов другого класса объект должен породить exception класса StackException.
Такие же exception должны возникать и в случае возникновения других ошибок,
например при чтении из пустого стека.
Stack должен содержать следующие функции:
push() - для добавления элемента в стек
pop() - функция возвращает последний элемент стека. при этом он удаляется из стека
is_empty() - возвращает True, если стек пустой, иначе False
clear() - очистка стека
Для объекта стек должна быть доступна функция len()
'''


class StackException(Exception):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}


class Stack:
    data = []
    type = None

    def __init__(self, sth):
        self.type = sth

    def push(self, obj):
        if type(obj) == self.type or issubclass(type(obj), self.type):
            self.data.append(obj)
        else:
            raise StackException(type(obj))

    def pop(self):
        if len(self.data) == 0:
            raise StackException(0)
        return self.data.pop()

    def clear(self):
        self.data.clear()

    def is_empty(self):
        return True if len(self.data) == 0 else False

    def __len__(self):
        return len(self.data)
