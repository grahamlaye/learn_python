import random

class Pin:
    def __init__(self):
        self.ids = {
             'Alice': {'PIN': 1234, 'Balance': 100},
             'Bob': {'PIN': 5678, 'Balance': 50000},
             'Jesus': {'PIN': 6666, 'Balance': 6666},
             'Nicky': {'PIN': 1234, 'Balance': 100000},
             'Harry': {'PIN': 1414, 'Balance': 0}
        }
        self.customer = random.choice(list(self.ids.keys()))
        self.customer_pin = self.ids[self.customer]['PIN']
        self.customer_balance = self.ids[self.customer]['Balance']
 
    def check_pin(self):
        self.entered_pin = int(input(f'Hello, {self.customer}, please enter PIN number: '))
        if self.entered_pin != self.customer_pin:
            return False
        else:
            print(f'Correct PIN for {self.customer}')
            self.check_balance()
            return True
    
    def check_balance(self):
        while True:
            print(f'Your balance is £{self.customer_balance} Would you like to make a withdrawal?\nEnter YES or NO')
            self.choice = str(input()).strip().upper()
            if self.choice == 'YES':
                self.withdrawal()
                break
            elif self.choice == 'NO':
                print(f'Stop wasting my time then, {self.customer}.')
                break
            else:
                print(f'{self.choice} Is an invalid choice')

    def withdrawal(self):
         self.withdrawal_amount = int(input('Enter amount in £ to withdraw: '))
         if self.withdrawal_amount <= self.customer_balance:
              self.customer_balance = self.customer_balance - self.withdrawal_amount
              print(f'Withdrawl of £{self.withdrawal_amount} processed. Your balance is now £{self.customer_balance}')
         else:
              print(f'You one broke ass mutha fucka, {self.customer}. You only got £{self.customer_balance}')
    
    def entry_point(self):
            attempts = 0
            attempts_limit = 3
            while attempts < attempts_limit:
                 if self.check_pin():
                      break
                 else:
                      attempts += 1
                      print(f'Incorrect PIN entered on attempt {attempts} of {attempts_limit}')
            if attempts >= attempts_limit:
                 print(f'{attempts} is too many incorrect attempts. Your card has been retained.')

if __name__ == "__main__":
    Pin().entry_point()