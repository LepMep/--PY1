from random import sample


def get_unique_list_numbers() -> list[int]:
    list_len = 15
    return sample(range(-10, 11), list_len)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
