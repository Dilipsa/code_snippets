"""
Decorators in Python are a powerful feature that allows you to 
modify or extend the behavior of functions or methods without changing their 
original code.
 
Decorators are higher-order functions that take a function as an argument and return 
another function. They are denoted by the `@decorator_name` syntax before a function 
definition.
"""
# Simple Decorator Example to Make Uppercase
def uppercase_decorator(func):
    def wrapper():
        result = func()  # Call the original function
        return result.upper()  # Convert the result to uppercase
    return wrapper

@uppercase_decorator
def get_string():
    return "My name is Dilip Sapkota"

print(get_string())  # Output: "MY NAME IS DILIP SAPKOTA"

"""
Create a decorator add_dec that adds an additional number entered by the user to 
the result of a function that adds two given numbers. The decorator will prompt 
the user to input a number, and the sum of this number with the result of the 
original function will be returned.
"""
def add_dec(func):
    def wrapper(num_one, num_two):
        num_three = int(input("Enter a number: "))  # Prompt user to input a number
        result = func(num_one, num_two)  # Call the original function
        result += num_three  # Add the additional number to the result
        return result
    return wrapper

@add_dec
def add_nums(num_one, num_two):
    return num_one + num_two

# Test the decorated function
print(add_nums(10, 20))  # Output: Sum of 10, 20, and the additional number entered by the user

"""
Create a decorator named `allow_delete` that restricts the execution of a function 
based on the user type. The decorator should only allow the function to execute if 
the user type matches "Admin". If the user type does not match, it should print a 
message indicating that the user is not authorized to perform the action.
"""
def allow_delete(user_type):
    def decorator(func):
        def wrapper():
            if user_type != "Admin":
                print("You are not authorised to perform this action.")
            else:
              return func()
        return wrapper
    return decorator

@allow_delete("Admin")
def delete_user():
    print("User deleted successfully")
delete_user()
