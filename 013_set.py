"""
Sets
==============================================================================================================
A Set is an unordered collection data type that is unindexed, mutable, and has no duplicate elements. 
Sets are created with curly braces {}
"""

# Create a set
# Use curly braces or the built-in set function.

my_set = {"apple", "banana", "cherry"}
print(my_set)
  # Output
  # {'banana', 'apple', 'cherry'}

# or use the set function and create from an iterable, e.g. list, tuple, string
my_set_2 = set(["one", "two", "three"])
my_set_2 = set(("one", "two", "three"))
print(my_set_2)
  # Output:
  # {'one', 'two', 'three'}

my_set_3 = set("Dilip")
print(my_set_3)
  # Output:
  # {'i', 'p', 'D', 'l'}

# careful: an empty set cannot be created with {}, as this is interpreted as dict
# use set() instead
a = {}
print(type(a))
  # Output:
    # <class 'dict'>
a = set()
print(type(a))
  # Output:
    # <class 'set'>

# Add elements
# =============================================================================================================
my_set = set()

# use the add() method to add elements
my_set.add(42)
my_set.add(True)
my_set.add("Hello")

# note: the order does not matter, and might differ when printed
print(my_set)
  # Output:
    # {True, 42, 'Hello'}

# nothing happens when the element is already present:
my_set.add(42)
print(my_set)
  # Output:
    # {True, 42, 'Hello'}

# Remove elements
# =============================================================================================================
# remove(x): removes x, raises a KeyError if element is not present
my_set = {"apple", "banana", "cherry"}
my_set.remove("apple")
print(my_set)
  # Output:
    # {'banana', 'cherry'}

# KeyError:
# my_set.remove("orange")

# discard(x): removes x, does nothing if element is not present
my_set.discard("cherry")
my_set.discard("blueberry")
print(my_set)
  # Output:
  #   {'banana'}

# clear() : remove all elements
my_set.clear()
print(my_set)
  # Output:
    # set()

# pop() : return and remove a random element
a = {True, 2, False, "hi", "hello"}
print(a.pop())
# Output:
  # False

print(a)
  # Output:
    # {True, 2, 'hi', 'hello'}