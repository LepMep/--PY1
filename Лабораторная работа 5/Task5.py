from random import sample
import string


def get_random_password(length=8) -> str:
    password = ""
    password_list = (sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, length))
    for item in password_list:
        password += item

    return password


print(get_random_password())
print(get_random_password(length=12))
