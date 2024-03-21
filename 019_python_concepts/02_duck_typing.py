"""
Duck typing is a concept in programming languages like Python 
where the type or class of an object is determined by its behavior rather 
than its explicit declaration. 
"""
class Duck:
    def quack(self):
        print("Quack! Quack!")

class Person:
    def quack(self):
        print("I'm not a duck, but I can quack like one!")

def make_quack(obj):
    obj.quack()

# Creating instances of Duck and Person classes
duck = Duck()
person = Person()

# Both duck and person can be passed to the make_quack function
make_quack(duck)    # Outputs: Quack! Quack!
make_quack(person)  # Outputs: I'm not a duck, but I can quack like one!
