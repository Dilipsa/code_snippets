"""
Tuples
============================================================================================================
A tuple is a collection of objects which is ordered and immutable. 
Tuples are similar to lists, the main difference ist the immutability. 
In Python tuples are written with round brackets and comma separated values.

data = ("Dilip", 34, "Bangalore", "Nescode Technology")

Reasons to use a tuple over a list

  Generally used for objects that belong together.
  Use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
  Since tuple are immutable, iterating through tuple is slightly faster than with list.
  Tuples with their immutable elements can be used as key for a dictionary. This is not possible with lists.
  If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

Creating tuple
  Example:
"""
tuple_1 = ("Dilip", 48, "Bangalore")
tuple_2 = "Melvin", 26, "Kerala" # Parentheses are optional

# Special case: a tuple with only one element needs to have a comma at the end, 
# otherwise it is not recognized as tuple
tuple_3 = (25,)
print(tuple_1) # ('Dilip', 48, 'Bangalore')
print(tuple_2) # ('Melvin', 26, 'Kerala')
print(tuple_3) # (25,)

# Or convert an iterable (list, dict, string) with the built-in tuple function
tuple_4 = tuple([1,2,3])
print(tuple_4) # (1, 2, 3)


"""
Access elements
You access the tuple items by referring to the index number. Note that the indices start at 0.
"""
item = tuple_1[0]
print(item)   # Dilip
# You can also use negative indexing, e.g -1 refers to the last item,
# -2 to the second last item, and so on
item = tuple_1[-1]
print(item)  # Bangalore

"""
Delete a tuple
  del tuple_2

Iterating
  # Iterating over a tuple by using a for in loop"""

for i in tuple_1:
    print(i)

"""
Output:
  Dilip
  48
  Bangalore
"""

"""
Check if an item exists
"""

if "Bangalore" in tuple_1:
    print("yes")
else:
    print("no")
"""
Output:
  yes
"""

"""
Usefule methods
"""

my_tuple = ('a','p','p','l','e',)

# len() : get the number of elements in a tuple
print(len(my_tuple))

# count(x) : Return the number of items that is equal to x
print(my_tuple.count('p'))

# index(x) : Return index of first item that is equal to x
print(my_tuple.index('l'))

# repetition
my_tuple = ('a', 'b') * 5
print(my_tuple)

# concatenation
my_tuple = (1,2,3) + (4,5,6)
print(my_tuple)

# convert list to a tuple and vice versa
my_list = ['a', 'b', 'c', 'd']
list_to_tuple = tuple(my_list)
print(list_to_tuple)

tuple_to_list = list(list_to_tuple)
print(tuple_to_list)

# convert string to tuple
string_to_tuple = tuple('Hello')
print(string_to_tuple)

"""
Output:
  5
  2
  3
  ('a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')
  (1, 2, 3, 4, 5, 6)
  ('a', 'b', 'c', 'd')
  ['a', 'b', 'c', 'd']
  ('H', 'e', 'l', 'l', 'o')
"""

"""
Slicing
==============================================================================================================
Access sub parts of the tuple wih the use of colon (:), just as with strings.
"""
# a[start:stop:step], default step is 1
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
b = a[::2] # start to end with every second item
print(b)
b = a[::-1] # reverse tuple
print(b)

"""
Output:
  (2, 3)
  (3, 4, 5, 6, 7, 8, 9, 10)
  (1, 2, 3)
  (1, 3, 5, 7, 9)
  (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
"""
"""
Unpack tuple
==============================================================================================================
"""
# number of variables have to match number of tuple elements
tuple_1 = ("Melvin", 28, "Kerla")
name, age, city = tuple_1
print(name)
print(age)
print(city)

# tip: unpack multiple elements to a list with *
my_tuple = (0, 1, 2, 3, 4, 5)
item_first, *items_between, item_last = my_tuple
print(item_first)
print(items_between)
print(item_last)

"""
Output:
  Melvin
  28
  Kerala
  0
  [1, 2, 3, 4]
  5  
"""
"""
Nested tuples
==============================================================================================================
"""
a = ((0, 1), ('age', 'height'))
print(a)
print(a[0])

"""
Output:
  ((0, 1), ('age', 'height'))
  (0, 1)
  """

"""
Compare tuple and list
==============================================================================================================
The immutability of tuples enables Python to make internal optimizations. 
Thus, tuples can be more efficient when working with large data.
"""
# compare the size
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

"""
Ouput:
  104 bytes
  80 bytes
"""

# compare the execution time of a list vs. tuple creation statement(Not understood code? Simply ignore it.)
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000)) # measures the time it takes to execute the creation of the list [0, 1, 2, 3, 4, 5] one million times.
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) # measures the time it takes to execute the creation of the tuple (0, 1, 2, 3, 4, 5) one million times.

"""
Output:
  0.04123792300015339   Second # this output will be based on your system configuration
  0.0074249979998057825 Second # this output will be based on your system configuration
"""

"""
1) List is a collection of items enclosed inside square brackets.
   Tuple is enclosed inside parenthesis and parenthsis are optional.

2) List consumes more memory than tuple for same data.

3) Tuple is faster in execution than list.

4) Comprehension is applicable to the list while not applicable to tuple

5) Use of tuple: to store read-only collection (immutibility)
   Use of list : to store modifiable collection (mutibility)
"""

# Create a tuple
my_tuple = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)

# Initialize an empty dictionary to store frequencies
frequency_dict = {}

# Iterate over the tuple elements
for element in my_tuple:
    # Increment the count for each element in the dictionary
    frequency_dict[element] = frequency_dict.get(element, 0) + 1

# Print the frequency of each element
for element, frequency in frequency_dict.items():
    print(f"Element {element}: Frequency {frequency}")
