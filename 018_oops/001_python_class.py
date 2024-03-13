"""
Instance Variable:
==============================================================================
Instance variables are variables that are unique to each instance of a class.
They are defined within the __init__ method using self. notation.
"""
class MyClass:
    def __init__(self, x):
        self.x = x

"""
Class Variable:
===============================================================================
Class variables are shared among all instances of a class.
They are defined outside of any method in the class.
"""
class MyClass:
    class_var = 10

"""
Instance Method:
===============================================================================
Instance methods operate on instances of a class.
They take self as the first parameter to refer to the instance itself.
"""
class MyClass:
    def instance_method(self):
        return self.x

"""
Class Method:
===============================================================================
Class methods operate on the class itself rather than instances.
They take cls as the first parameter to refer to the class.
"""
class MyClass:
    @classmethod
    def class_method(cls):
        return cls.class_var

"""
Static Method:
===============================================================================
Static methods are independent of the class and the instance.
They are defined using @staticmethod decorator.
"""
class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method"

"""
Alternative Constructor:
===============================================================================
Alternative constructors are class methods that provide alternative 
ways to create instances of a class.
"""
class MyClass:
    @classmethod
    def from_string(cls, str):
        # Parse the string and return an instance
        return cls(parsed_data)

"""
Property:
==============================================================================
Properties provide a way of customizing attribute access. 
They allow you to define special methods to manage attribute access, 
such as getting, setting, or deleting attributes. This enables you to 
add custom behavior when accessing attributes of an object.


"""
class MyClass:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

obj = MyClass(5)
print(obj.x)  # Output: 5

"""
Getter:
=============================================================================
Getters are methods that get the value of a property. In Python, getters are often 
implemented using the @property decorator. They provide a way to retrieve the value 
of a property, usually by returning a value derived from the object's internal state.
"""
class MyClass:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

obj = MyClass(5)
print(obj.x)  # Output: 5

"""
Setter:
=============================================================================
Setters are methods that set the value of a property. In Python, setters are 
defined using <property_name>.setter decorator. They provide a way to update 
the value of a property, usually by modifying the object's internal state.
"""
class MyClass:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

obj = MyClass(5)
print(obj.x)  # Output: 5

obj.x = 10  # This calls the setter method
print(obj.x)  # Output: 10
