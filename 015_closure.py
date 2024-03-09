"""
A closure in Python refers to a function object that remembers values from its 
enclosing lexical scope even when the scope is no longer available. In other words, 
a closure allows a function to retain access to variables from its enclosing scope, 
even after the scope has finished executing.
"""
def outer_function(x):
    # This is the enclosing function
    def inner_function(y):
        # This is the nested function
        return x + y  # inner_function has access to the variable x from the outer_function's scope

    return inner_function  # Return the nested function without calling it

# Create a closure by calling outer_function with argument 10
closure = outer_function(10)

# Call the closure with argument 5
result = closure(5)  # This will return 10 + 5 = 15

print(result)  # Output: 15
