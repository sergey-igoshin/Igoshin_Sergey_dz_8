"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:
email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
имеет ли смысл в данном случае использовать функцию re.compile()?
"""
import re


def email_parse(email_address):
    RE_EMAIL = re.findall(r'(^[^@&][a-z0-9_\.-]*)@([a-z0-9_-]*\.[a-z]{2,})$', email_address)
    if not RE_EMAIL:
        raise ValueError(f'Неправильный адрес E-mail: {email_address}')
    return dict(zip(['username', 'domain'], RE_EMAIL[0]))


try:
    print(email_parse(input('Введите E-mail: ').lower()))
except ValueError as err:
    print(err)
