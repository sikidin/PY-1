import string
from random import sample

n = 8  # количество символов в пароле

def get_random_password() -> str:
    letters_ = string.ascii_lowercase  # получаем строку с буквами a-z
    letters_1 = string.ascii_uppercase  # получаем строку с буквами A-Z
    digits = string.digits  # получаем строку 0-9

    return ''.join(sample(''.join([letters_1, letters_, digits]), n))


print(get_random_password())

