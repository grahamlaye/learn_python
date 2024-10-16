# A really simple function
def simple_function():
    print('This is a function. It will run when called')
    # It can do lots of stuff inside it.
    print(5 + 5)

# When we call the function, it runs.
simple_function()

# This is a function with a parameter. Parameters can be whatever we want.
def simple_function_paramter(my_number):
    print(f'This is another simple function that uses a parameter. When we call the function we pass {my_number} as an argument.')
    print(my_number + 5)

# Call the above function
simple_function_paramter(10)

# This is a similar function but uses a string instead of an integer as the parameter and argument.
def simple_function_string_paramater(my_string):
    print(f'Functions can accept lots of different data types. Here we are using a string')
    print(f'My name is: {my_string}')

# Call the above function
simple_function_string_paramater('Harry')

# This is a function with two parameters
def simple_function_two_params(my_name, my_age):
    print(f'My name is: {my_name}. I am {my_age} years old')

# Call the above function
simple_function_two_params('Harry', 14)

# We can use the input method to enter the arguments dynamically
def function_with_input():
    my_name = input('Enter your name: ')
    my_age = input('Enter your age: ')
    print(f'My name is {my_name}. I am {my_age} years old.')

# Call the above function. This time we set the arguments WITHIN the function itself.
function_with_input()

# We can also use iteration in Python.
def iterate_list(my_list):
    for item in my_list:
        print(item)

# Define a list
list_of_names = ['Graham', 'Mum', 'Harry', 'Becca', 'Charn', 'Katie', 'Nancy', 'Alfie', 'Maggie', 'Archie']
massive_list = list(range(1, 10001))

# Call the above function with list of names as an argument.
iterate_list(list_of_names)

# Call the same function with a massive list of numbers
iterate_list(massive_list)

# Functions are super powerful because we can reuse the same code without having to retype it every time.