"""
Functions in Python are blocks of reusable code that perform a specific task. 
They allow you to break down your program into smaller, manageable pieces. 
Here's a comprehensive overview of functions in Python:

"""
# Defining Functions:
def foo():
    # Function body
    pass

# Function Parameters:
def greet(name):
    print("Hello, " + name)

greet("Dilip")

# Default Parameters:
def greet(name="World"):
    print("Hello, " + name)

greet()         # Outputs: Hello, World
greet("Dilip")  # Outputs: Hello, Dilip

# Arbitrary Arguments:
def greet(*names):
    for name in names:
        print("Hello, " + name)

greet("Dilip", "Kushal")  # Outputs: Hello, Dilip
                          #          Hello, Kushal

# Returning Values:
def add(x, y):
    return x + y

result = add(3, 5)
print(result)  # Outputs: 8

# Multiple Return Values:
def get_info():
    return "Dilip", 30

name, age = get_info()
print(name, age)  # Outputs: Dilip 30


"""
Scope and Lifetime:
Local Variables:
Variables declared inside a function have a local scope and are only accessible within that function.

Global Variables:
Variables declared outside of any function have a global scope and are accessible from anywhere in the program.

Nonlocal Variables:
Used in nested functions, indicating that the variable is not local to the inner function, nor is it global.


Arguments and parameters
=========================

Parameters are the variables that are defined or used inside parentheses while defining a function
Arguments are the value passed for these parameters while calling a function
def print_name(name): # name is the parameter
    print(name)

print_name('Dilip') # 'Dilip' is the argument
 Output:
 Dilip

Positional and keyword arguments
====================================================
We can pass arguments as positional or keyword arguments. 
Some benefits of keyword arguments can be: - We can call arguments by their names to 
make it more clear what they represent - We can rearrange arguments in a way that 
makes them most readable
"""

def letters(a, b, c):
    print(a, b, c)

# positional arguments
letters(1, 2, 3)

# keyword arguments
letters(a=1, b=2, c=3)
letters(c=3, b=2, a=1) # Note that the order is not important here

# mix of both
letters(1, b=2, c=3)

# This is not allowed:
# letters(1, b=2, 3) # positional argument after keyword argument
# letters(1, b=2, a=3) # multiple values for argument 'a'

# Output:
#     1 2 3
#     1 2 3
#     1 2 3
#     1 2 3

"""
Default arguments
=============================================
Functions can have default arguments with a predefined value. 
This argument can be left out and the default value is then passed to the function, 
or the argument can be used with a different value. Note that default arguments must 
be defined as the last parameters in a function.
"""

# default arguments
def letters(a, b, c, d=4):
    print(a, b, c, d)

letters(1, 2, 3, 4)
letters(1, b=2, c=3, d=100)

# not allowed: default arguments must be at the end
# def letters(a, b=2, c, d=4):
#     print(a, b, c, d)

# Output:
#     1 2 3 4
#     1 2 3 100

"""
Variable-length arguments (*args and **kwargs)
==============================================

If you mark a parameter with one asterisk (*), 
you can pass any number of positional arguments to your function (Typically called *args)

If you mark a parameter with two asterisks (**), 
you can pass any number of keyword arguments to this function (Typically called **kwargs).
"""

def letters(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])

# 3, 4, 5 are combined into args
# six and seven are combined into kwargs
letters(1, 2, 3, 4, 5, six=6, seven=7)
print()

# omitting of args or kwargs is also possible
letters(1, 2, three=3)

# Output:
#     1 2
#     3
#     4
#     5
#     six 6
#     seven 7

#     1 2
#     three 3

"""
Forced keyword arguments
Sometimes you want to have keyword-only arguments. 
You can enforce that with: - If you write '*,' in your function parameter list, 
all parameters after that must be passed as keyword arguments. 
- Arguments after variable-length arguments must be keyword arguments.
"""

def letters(a, b, *, c, d):  # After * it should be keyword arguments
    print(a, b, c, d)

letters(1, 2, c=3, d=4)
# not allowed:
# letters(1, 2, 3, 4)

# arguments after variable-length arguments must be keyword arguments
def letters(*args, last):
    for arg in args:
        print(arg)
    print(last)

letters(8, 9, 10, last=50)

# Output:
#     1 2 3 4
#     8
#     9
#     10
#     50

""""
Unpacking into agruments
========================================================================
Lists or tuples can be unpacked into arguments with one asterisk (*) 
if the length of the container matches the number of function parameters.

Dictionaries can be unpacked into arguments with two asterisks (**) 
the the length and the keys match the function parameters.
"""

def letters(a, b, c):
    print(a, b, c)

# list/tuple unpacking, length must match
my_list = [4, 5, 6] # or tuple
letters(*my_list)

# dict unpacking, keys and length must match
my_dict = {'a': 1, 'b': 2, 'c': 3}
letters(**my_dict)

# my_dict = {'a': 1, 'b': 2, 'd': 3} # not possible since wrong keyword

# Output:
#     4 5 6
#     1 2 3

"""
Local vs global variables
===============================
Global variables can be accessed within a function body, but to modify them, 
we first must state global var_name in order to change the global variable.
"""

def func():
    x = number # global variable can only be accessed here
    print('number in function:', x)

number = 0
func()

# modifying the global variable
def func_two():
    global number # global variable can now be accessed and modified
    number = 3

print('number before func_two(): ', number)
func_two() # modifies the global variable
print('number after func_two(): ', number)

# Output:
#     number in function: 0
#     number before func_two():  0
#     number after func_two():  3

"""
If we do not write global var_name and asign a new value to a variable with the same 
name as the global variable, this will create a local variable within the function. 
The global variable remains unchanged.
"""

number = 0

def func_three():
    number = 3 # this is a local variable

print('number before func_three(): ', number)
func_three() # does not modify the global variable
print('number after func_three(): ', number)

# Output:
#     number before func_three():  0
#     number after func_three():  0


"""
Parameter passing
====================================
"""

def sum(num1, num2):
    return num1 + num2

first = 20
second = 30

print(sum(10, 20))        # passed object by value
print(sum(first, second)) # passed object by reference