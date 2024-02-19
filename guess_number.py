from random import randint
number = randint(1,100)
print('Угадай число, чушпан >:D')

while True:
    guess = int(input('Введи число: '))
    if guess > number:
        print('Не угадал, твое число больше kekw')
    if guess < number:
        print('Не угадал, твое число меньше xD')
    if guess == number:
        break
print('Повезло тебе, теперь ты Пацан, а вокруг враги') 