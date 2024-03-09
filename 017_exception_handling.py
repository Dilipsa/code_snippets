"""
Exception Handling
================================================================================
Exceptions are raised when the program is syntactically correct, but the code results 
in an error. This error does not stop the execution of the program, however, it changes 
the normal flow of the program.

There are several built-in Python exceptions that can be raised when an error occurs 
during the execution of a program. Here are some of the most common types of 
exceptions in Python:

SyntaxError: 
  This exception is raised when the interpreter encounters a syntax error in the code, 
  such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: 
  This exception is raised when an operation or function is applied to an object of the 
  wrong type, such as adding a string to an integer.
NameError: 
  This exception is raised when a variable or function name is not found in the current 
  scope.
IndexError: 
  This exception is raised when an index is out of range for a list, tuple, or other 
  sequence types.
KeyError: 
  This exception is raised when a key is not found in a dictionary.
ValueError: 
  This exception is raised when a function or method is called with an invalid 
  argument or input, such as trying to convert a string to an integer when the string 
  does not represent a valid integer.
AttributeError: 
  This exception is raised when an attribute or method is not found on an object, 
  such as trying to access a non-existent attribute of a class instance.
IOError: 
  This exception is raised when an I/O operation, such as reading or writing a file, 
  fails due to an input/output error.
ZeroDivisionError: 
  This exception is raised when an attempt is made to divide a number by zero.
ImportError: 
  This exception is raised when an import statement fails to find or load a module.

  
Try-Except Blocks
======================================================================================
The most common way to handle exceptions in Python is by using try and except blocks. 
Code that might raise an exception is placed within the try block, 
and potential exception handling code is placed within the except block.
"""
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Exception handling code
    print("Error: Division by zero")


"""
Handling Multiple Exceptions
======================================================================================
"""
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Exception handling code for ZeroDivisionError
    print("Error: Division by zero")
except ValueError:
    # Exception handling code for ValueError
    print("Error: Invalid value")
except (TypeError, IndexError):
    # Exception handling code for TypeError or IndexError
    print("Error: Type or index error")

"""
Handling All Exceptions
====================================================================================
"""
try:
    # Code that might raise an exception
    result = 10 / 0
except:
    # Generic exception handling code
    print("An error occurred")

"""
Finally Block
=====================================================================================
The else block is executed if no exception occurs in the try block. 
"""
try:
    # Code that might raise an exception
    result = 10 / 2
except ZeroDivisionError:
    # Exception handling code
    print("Error: Division by zero")
else:
    # Code to execute if no exception occurs
    print("Division successful:", result)

"""
Finally Block
=====================================================================================
You can use a finally block to execute cleanup code that should always run, 
regardless of whether an exception occurs or not. This is useful for releasing 
resources, closing files, or cleaning up connections
"""
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Exception handling code
    print("Error: Division by zero")
else:
    # Code to execute if no exception occurs
    print("Division successful:", result)
finally:
    # Cleanup code
    print("Cleanup code executed")




try:
    num = int(input("Enter a number:"))
    num2_input = input("Enter a number:")
    try:
        num2 = int(num2_input)
        print(num / num2)
    except ValueError:
        print("Please enter a valid number.")
except ZeroDivisionError as e:
    print("Error:", e)
