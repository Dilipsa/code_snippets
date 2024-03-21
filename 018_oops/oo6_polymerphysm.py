class Animal:
    def speak(self):
        pass  # Placeholder method, to be overridden in subclasses

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Function to make animals speak
def make_animal_speak(animal):
    return animal.speak()

# Creating instances of different animals
dog = Dog()
cat = Cat()
cow = Cow()

# Making animals speak
print(make_animal_speak(dog))  # Output: Woof!
print(make_animal_speak(cat))  # Output: Meow!
print(make_animal_speak(cow))  # Output: Moo!

# ===================================================================================================================
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def withdraw(self, amount):
        raise NotImplementedError("Subclasses must implement this method")


class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds in savings account!")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} from savings account successful. Remaining balance: {self.balance}")


class CheckingAccount(Account):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds in checking account!")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} from checking account successful. Remaining balance: {self.balance}")


class InvestmentAccount(Account):
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds in investment account!")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} from investment account successful. Remaining balance: {self.balance}")


# Function to make a withdrawal from any account type
def make_withdrawal(account, amount):
    account.withdraw(amount)


# Creating instances of different account types
savings_account = SavingsAccount("SA001", 5000)
checking_account = CheckingAccount("CA001", 3000)
investment_account = InvestmentAccount("IA001", 10000)

# Making withdrawals from each account type
make_withdrawal(savings_account, 2000)      # Output: Withdrawal of 2000 from savings account successful. Remaining balance: 3000
make_withdrawal(checking_account, 4000)    # Output: Insufficient funds in checking account!
make_withdrawal(investment_account, 12000)  # Output: Insufficient funds in investment account!

# =========================================================================================================================
# Dynamic polymerphysm
# =========================================================================================================================
class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


def make_animal_speak(animal):
    animal.speak()


# Creating instances of different animals
animal = Animal()
dog = Dog()
cat = Cat()

# Making animals speak
make_animal_speak(animal)  # Output: Animal speaks
make_animal_speak(dog)     # Output: Dog barks
make_animal_speak(cat)     # Output: Cat meows

# =========================================================================================================================
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Function to calculate area for any shape
def calculate_area(shape):
    return shape.area()


# Creating instances of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4)

# Calculating areas for each shape
print("Area of the circle:", calculate_area(circle))       # Output: Area of the circle: 78.53981633974483
print("Area of the rectangle:", calculate_area(rectangle)) # Output: Area of the rectangle: 24
print("Area of the triangle:", calculate_area(triangle))   # Output: Area of the triangle: 6.0



import types

class User:
    def print_name(self):
        print("Dilip")

    def get_info(self):
        print("Previously, I was not part of User class but now I am")

# Create an instance of User
dilip = User()

# Dynamically assign a different method to the print_name attribute
dilip.print_name = types.MethodType(User.get_info, dilip)

# Now calling the print_name method, which was reassigned
dilip.print_name()  # Output: Previously, I was not part of User class but now I am
