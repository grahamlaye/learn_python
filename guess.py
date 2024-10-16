import random

class Guess:
    def __init__(self):
        self.attempts = 0
        self.magic_number = random.randint(1,100)

    def the_game_loop(self):
        while True:
            self.current_guess = int(input('Enter your guess: '))
            self.attempts += 1

            if self.current_guess > self.magic_number:
                print(f'Lower than {self.current_guess}')
            elif self.current_guess < self.magic_number:
                print(f'Higher than {self.current_guess}')
            else:
                print(f'Yes, your guess {self.current_guess} is the magic number of {self.magic_number} after {self.attempts} attempts')
                break


Guess().the_game_loop()
