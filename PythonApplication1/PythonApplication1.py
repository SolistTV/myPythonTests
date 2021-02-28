import random
import requests


def good_password_gen(length=10):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+-=\'\\\"'
    alphabet = letters + upper_letters + numbers + symbols

    password = ''
    for i in range(length):
        password += random.choice(alphabet)

    # print('Сгенерирован пароль' + length + ' символов')
    return password


counter = 0


def bad_password_gen():
    global counter
    passwords = """password
123456
12345678
1234
qwerty
12345
dragon
pussy
baseball
football"""

    popular_passwords = passwords.split('\n')
    counter += 1
    while counter >= len(popular_passwords):
        counter = counter - len(popular_passwords)

    return popular_passwords[counter]


while True:
    password = bad_password_gen()
    response = requests.post('http://127.0.0.1:')

print(good_password_gen(6))
print(good_password_gen(7))
print(good_password_gen(8))
