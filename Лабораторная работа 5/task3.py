from random import randint
a = 15
def get_unique_list_numbers() -> list[int]:
    random_list = [randint(-10, 10) for _ in range(a)]
    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))



