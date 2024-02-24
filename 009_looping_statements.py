"""
Looping Statements:
===============================================================================================================
A looping statement, also known as a loop, is a fundamental programming construct that allows you
to execute a block of code repeatedly based on a specified condition or a predefined number of iterations. 
Loops are used to automate repetitive tasks, iterate over collections of data, 
and perform computations efficiently.

Looping Techniques:
===============================================================================================================
Using range():
===============================================================================================================
Generating numerical sequences.

Using enumerate(): 
===============================================================================================================
Iterating over both indices and elements of a sequence.

Using zip(): 
===============================================================================================================
Iterating over multiple sequences simultaneously.
Loops are powerful tools in programming and are used extensively to perform repetitive tasks efficiently. 
Understanding how to use loops effectively is essential for any beginner programmer.


1. for Loops:
===============================================================================================================
A for loop is used to iterate over a sequence (such as a list, tuple, string, or range) 
or any other iterable object.
===============================================================================================================
Syntax:
  for item in iterable:
    # code to execute for each item

Example:
  fruits = ["apple", "banana", "cherry"]
  for fruit in fruits:
      print(fruit)

Output:
  apple
  banana
  cherry

2. while Loops:
===============================================================================================================
A while loop repeats a block of code as long as a specified condition is true.
Syntax:
  while condition:
    # code to execute as long as condition is true

Example:
  count = 0
  while count < 5:
      print(count)
      count += 1

Output:
  0
  1
  2
  3
  4

  
Common Loop Control Statements:
===============================================================================================================
break: 
  Terminates the loop prematurely, without executing the rest of the code inside the loop.

continue: 
  Skips the rest of the code inside the loop for the current iteration and proceeds to the next iteration.

pass: 
  Placeholder that does nothing when executed. 
  It's often used as a placeholder when a statement is syntactically required but 
  you don't want any code to execute.

  
Nested Loops:
===============================================================================================================
Loops can be nested inside each other. This means you can put one loop inside another loop.
Example:
  for i in range(3):
      for j in range(2):
          print(i, j)

Output:
  0 0
  0 1
  1 0
  1 1
  2 0
  2 1

"""

