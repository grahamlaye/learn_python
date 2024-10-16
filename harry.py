import random


def guess_the_number():
    magic_number = random.randint(1,10)
    my_attempts = 0

    while True:
        my_guess = int(input('Guess the number: '))
        my_attempts += 1
        if magic_number == my_guess:
            print(f'Yes, {my_guess} is the correct answer after {my_attempts} attempts.')
            break
        elif my_guess > magic_number:
            print(f'No, your guess {my_guess} is too high after {my_attempts} attempts.')
        elif my_guess < magic_number:
            print(f'No, your guess {my_guess} is too low after {my_attempts} attempts.')
        else:
            exit('Something weird happened.')


guess_the_number()