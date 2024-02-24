"""
enumerate():
==============================================================================================================
The enumerate() function in Python is used to iterate over a sequence while keeping track of the 
index of each item. It returns an enumerate object, which yields pairs of indices and corresponding 
values from the sequence.

Syntax:
  enumerate(iterable, start=0)

  iterable: The sequence or iterable object over which you want to iterate.
  start (optional): The index at which to start the numbering. It defaults to 0.

Example:
  fruits = ["apple", "banana", "cherry"]
  for index, fruit in enumerate(fruits):
      print(index, fruit)

  Output:
  0 apple
  1 banana
  2 cherry
  

Specifying a Start Index:
==============================================================================================================
You can also specify the starting index for enumeration using the start parameter.

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

Output:
1 apple
2 banana
3 cherry


next():
==============================================================================================================
next() is another built-in Python function used with iterators. It retrieves the next item from an iterator.

fruits = ["apple", "banana", "cherry"]
enum_fruits = enumerate(fruits)
print(next(enum_fruits))  # Output: (0, 'apple')
print(next(enum_fruits))  # Output: (1, 'banana')
print(next(enum_fruits))  # Output: (2, 'cherry')

"""