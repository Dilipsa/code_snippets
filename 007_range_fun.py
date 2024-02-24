"""
range()
===============================================================================================================
The range() function in Python is used to generate a sequence of numbers. 
It's commonly used in loops to iterate a specific number of times or to generate indices 
for accessing elements in a sequence like lists, tuples, or strings. Here's all you need 
to know about the range() function:

range([start], stop, [step])

start (optional): The starting value of the sequence. If omitted, it defaults to 0.
stop: The end value of the sequence (exclusive). The range() function generates numbers up to, but not including, this value.
step (optional): The increment between each number in the sequence. If omitted, it defaults to 1.

Examples:
  1] Generating a sequence of numbers from 0 to n-1:
  ============================================================================================================
    for i in range(5):
      print(i)

    Output:
    0
    1
    2
    3
    4

  2] Generating a sequence of numbers from a specified start to end (exclusive):
  ============================================================================================================
    for i in range(2, 8):
      print(i)

    Output:
    2
    3
    4
    5
    6
    7

  3] Generating a sequence of numbers with a specified step:
  ============================================================================================================
    for i in range(1, 10, 2):
      print(i)

    Output:
    1
    3
    5
    7
    9

  4] Using range() to create a list:
  ============================================================================================================
    numbers = list(range(5))
      print(numbers)

    Output:
    [0, 1, 2, 3, 4]

"""