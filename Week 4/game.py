import random

while True:
    try:
        n = int(input('Level:'))
        if n > 0:
            break
        else:
            pass
    except ValueError:
        pass
number = random.randint(1,n)

while True:
    try:
        guess = int(input('Guess:'))
        if guess <= 0:
            pass
        elif 0 <= guess < number:
            print('Too small!')
            pass
        elif guess > number:
            print('Too large!')
            pass
        else :
            print('Just right!')
            print('')
            break
    except ValueError:
        pass