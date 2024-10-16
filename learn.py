
'''
help(print)

rng = range(2, 12, 2)

print(list(rng))

print(rng)

#help(range)
'''
#x = 4
#sumz = (lambda x: x + x)
#print(sumz(x))

#numbz = [1,2,3,4,5,6,7,8,9,10]
#evens = (list(range(2,101, 1))); print(evens)
#odds = list(range(1, 101, 2)); print(odds)

# Random words
# CBA
#import random, string
#words = random.randint(4,10)
#print(words)

occupants = [
    {"Name": "Harry", "Age": 14},
    {"Name": "Graham", "Age": 45},
    {"Name": "Archie", "Age": 7},
    {"Name": "Nicky", "Age": 45},
    {"Name": "Becca", "Age": 18},
    {"Name": "Maggie", "Age": 4}
]

occupants_dict = {
    "Harry": 14,
    "Graham": 45,
    "Archie": 7,
    "Nicky": 45,
    "Becca": 18,
    "Maggie": 4
}

def sort_it(payload=occupants):
    by_age = sorted(payload, key=lambda payload: payload["Age"], reverse=False)
    from pprint import pprint as pp
    pp(by_age)
    return(by_age)

#sort_it()

tasks = ['Wake up', 'Get dressed', 'Brush teeth', 'Drink coffee', 'Do work', 'Try not to play football manager', 'walk dogs', 'go to gym', 'tidy up']

# Enumerate stuff
def create_list(ret='yes'):
        if ret == "yes":
            formatted_tasks = []
            for index, task in enumerate(tasks):
                formatted_tasks.append(f"{index + 1}. {task}")
            return "\n".join(formatted_tasks)
        if ret == "no":
            for index, task in enumerate(tasks):
                print(f"{index +1}. {task}")

create_list()

# Use with context manager to correctly handle file operations (opens and closes without worrying about it)
with open('test.txt', 'w') as f:
    f.write(create_list())

with open('test.txt', 'r') as f:
     print(f.read())

import antigravity