"""
Python Generators
=======================================================================================
Generators are iterators, but you can only iterate over them once. 
It's because they do not store all the values in memory, they generate the values on 
the fly. You use them by iterating over them, either with a `for` loop or by passing 
them to any function or construct that iterates. Most of the time generators are 
implemented as functions. However, they do not return a value, they yield it.
"""
   
# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simple_generator(): 
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function 
for value in simple_generator():  
    print(value)


# A Python program to demonstrate use of 
# generator object with next() 

# A generator function 
def simple_generator(): 
	yield 1
	yield 2
	yield 3

# x is a generator object 
x = simple_generator() 

# Iterating over the generator object using next 

# In Python 3, __next__() 
print(next(x))  # or x.__next__() 
print(next(x))  # or x.__next__() 
print(next(x))  # or x.__next__() 



"""Advantages of Using Generator Functions in Python"""

# Generator function to generate even numbers
def even_numbers_generator(n):
    """Generate even numbers up to n."""
    for i in range(0, n, 2):
        yield i

# Function to generate even numbers and store in a list
def even_numbers_list(n):
    """Generate even numbers up to n and store in a list."""
    even_numbers = []
    for i in range(0, n, 2):
        even_numbers.append(i)
    return even_numbers

# Testing the memory usage
import sys

# Number of even numbers to generate
n = 1000000

# Using generator
even_gen = even_numbers_generator(n)
gen_mem_usage = sys.getsizeof(even_gen)

# Using list
even_list = even_numbers_list(n)
list_mem_usage = sys.getsizeof(even_list)

print(f"Memory used by generator: {gen_mem_usage} bytes")
print(f"Memory used by list: {list_mem_usage} bytes")


"""
Python Generator Exception Handling
======================================================================================
"""
def simple_generator():
    """Generator function to yield numbers from 0 to 2."""
    for i in range(3):
        yield i

# Create a generator object
generator_obj = simple_generator()

try:
    # Iterating over the generator object using next()
    print(next(generator_obj))  # or generator_obj.__next__()
    print(next(generator_obj))  # or generator_obj.__next__()
    print(next(generator_obj))  # or generator_obj.__next__()
    print(next(generator_obj))  # or generator_obj.__next__()
except StopIteration:
    print("Generator exhausted.")
except Exception as e:
    print("An error occurred:", e)
