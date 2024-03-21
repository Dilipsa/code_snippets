"""
Dynamic Function Assignment in Python / Dynamically Changing Method Behavior in Python,
concept of dynamic method binding or dynamic dispatch
"""
# Example 1
# ===========================================
class A:
  def greet(self):
    print("good morning from greet() function")

def func_greet():
    print("good morning from func_greet() function")


obj = A()
obj.greet = func_greet
obj.greet()

# Example 2
# ==========================================
class Dog:
    def bark(self):
        print("Woof! I'm a dog.")

def meow():
    print("Meow! I'm pretending to be a cat.")

# Create an instance of the Dog class
my_dog = Dog()

# Initially, the dog barks
my_dog.bark()

# Now, dynamically change the behavior of the bark method
my_dog.bark = meow

# After dynamically changing the method, the dog now meows
my_dog.bark()
