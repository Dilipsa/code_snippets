"""
Conditional Statements:
===============================================================================================================
1] if statement: This is the most basic conditional statement. 
It executes a block of code if a specified condition is true.
===============================================================================================================
if condition:
    # code to execute if condition is true

Example:
    x = 10
    if x > 5:
        print("x is greater than 5")

        
2] if-else statement: This statement allows you to execute one block of code if the condition is true 
and another block of code if the condition is false.
===============================================================================================================
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false

Exaxmple:
    x = 10
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")

        
3] if-elif-else statement: This is used when you have multiple conditions to check. 
   It allows you to check multiple conditions and execute a block of code 
   corresponding to the first true condition encountered. 
   If none of the conditions are true, the else block (if provided) will execute.
===============================================================================================================
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
else:
    # code to execute if none of the conditions are true

Example:
    x = 10
    if x > 10:
        print("x is greater than 10")
    elif x < 10:
        print("x is less than 10")
    else:
        print("x is equal to 10")
    
        
4] Nested if statements: You can nest if statements within other if statements to create more complex 
conditional logic.
===============================================================================================================
if condition1:
    if condition2:
        # code to execute if both condition1 and condition2 are true
    else:
        # code to execute if condition1 is true but condition2 is false

Example:
    x = 10
    if x > 5:
        if x < 15:
            print("x is between 5 and 15")


5] Ternary operator: Provides a compact way to write simple if-else statements in a single line.
===============================================================================================================
variable = value_if_true if condition else value_if_false
Example:
    x = 10
        result = "Even" if x % 2 == 0 else "Odd"

        
Else statement with for/while loop
With For Loop:
===============================================================================================================

In Python, you can use the else statement with a loop to execute a block of code when the loop 
completes normally, i.e., without encountering a break statement. This can be useful for executing 
cleanup code or handling situations where the loop terminates naturally.

Syntax:
    for item in iterable:
        # code to execute for each item
    else:
        # code to execute when the loop completes normally

Example:
    for num in range(2, 10):
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")

Output:
    2 is a prime number
    3 is a prime number
    4 is not a prime number
    5 is a prime number
    6 is not a prime number
    7 is a prime number
    8 is not a prime number
    9 is not a prime number

With While Loop:
==============================================================================================================
We can use the else statement with a while loop in Python. 
The else block associated with a while loop will execute when the loop condition becomes 
false, i.e., when the loop terminates naturally because the condition evaluates to False.

Syntax:
    while condition:
        # code to execute as long as condition is true
    else:
        # code to execute when the loop terminates naturally

Example:
    count = 0
    while count < 5:
        print(count)
        count += 1
    else:
        print("Loop completed successfully")

Output:
    0
    1
    2
    3
    4
    Loop completed successfully

"""