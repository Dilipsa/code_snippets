"""
Protected Access Modifier:
=====================================================================================================
Protected members are accessible within the class in which they are declared and by subclasses.
They are not accessible directly from outside the class hierarchy (i.e., from unrelated classes).
In Python, protected members are denoted by prefixing the member name with a single underscore (_).
"""
class Base: 
	def __init__(self): 

		# Protected member 
		self._a = 2

# Creating a derived class 
class Derived(Base): 
	def __init__(self): 

		# Calling constructor of 
		# Base class 
		Base.__init__(self) 
		print("Calling protected member of base class: ", self._a) 

		# Modify the protected variable: 
		self._a = 3
		print("Calling modified protected member outside class: ", self._a) 

obj1 = Derived() 
obj2 = Base() 

# Calling protected member 
# Can be accessed but should not be done due to convention 
print("Accessing protected member of obj1: ", obj1._a) 

# Accessing the protected variable outside 
print("Accessing protected member of obj2: ", obj2._a) 




