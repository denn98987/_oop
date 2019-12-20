'''
Телефонный номер состоит из 10 цифр, но пользователи могут номер вводить рзными способами,
такими как +79007878723, 8(905)56-344-23.
Создать функцию prepare_phone_number(phone: str)→ str,
которая принимает телефонный номер в виде строки, проверяет его валидность
и возвращает номер в виде +7 (900) 123-45-67.
Если заданный номер не валидный, функция возвращает exception класса PhoneNumberException
Валидный телефонный номер содержит 10 или 11 цифр, начинаться может с +7, 7 или 8,
содержит цифры, скобки. пробелы, табуляции и тире. Все остальные номера считаются не валидными.
'''
import re


class PhoneNumberException(Exception):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}


def prepare_phone_number(phone: str)-> str:
    if isinstance(phone, int):
        raise PhoneNumberException(phone)
    phone = phone.replace(' ', '')
    regex = r"^((\+7|7|8)-?)?((\(9\d{2}\))|(9\d{2}))-?(((\d{3})-?(\d{2})-?(\d{2}))|(\d{2})-?(\d{2})-?(\d{3}))$"
    matches = re.match(regex, phone)
    if matches is None:
        raise PhoneNumberException(phone)
    grps = matches.groups()
    nineHundreds = grps[2] if grps[2][0] == '(' else "("+grps[2]+")"
    othernums = (grps[7] or grps[10]) + (grps[8] or grps[11]) + (grps[9] or grps[12])
    return "+7 " + nineHundreds + " " + othernums[0:3] + '-' + othernums[3:5] + '-' + othernums[5:]

print(prepare_phone_number("8-900-782-31-21"))