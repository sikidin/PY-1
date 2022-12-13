from string import ascii_lowercase, ascii_uppercase, digits
from random import sample


def get_random_password(n=8) -> str:
    return ''.join(sample(''.join([ascii_lowercase+ascii_uppercase+digits]), n))


print(get_random_password())

