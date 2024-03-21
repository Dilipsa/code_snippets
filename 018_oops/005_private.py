"""
Private Access Modifier:
=====================================================================================================
Private members are accessible only within the class in which they are declared.
They cannot be accessed directly from outside the class, not even by subclasses.
"""
class User:
    def __init__(self, username, password):
        self.__username = username  # Private attribute
        self.__password = password  # Private attribute

    def __encrypt_password(self):
        # This method would perform encryption on the password
        print("Encrypting password...")

    def login(self, username, password):
        # Check if the provided username and password match
        if username == self.__username and password == self.__password:
            self.__encrypt_password()  # Call private method upon successful login
            print("Login successful.")
        else:
            print("Invalid username or password.")

# Example usage:
user1 = User("user123", "password123")

# Attempting to access private attribute and method from outside the class
# print(user1.__username)  # This line would raise an AttributeError
# user1.__encrypt_password()  # This line would raise an AttributeError

# Proper way to access the attributes and method
user1.login("user123", "password123")


class User: 
    def __init__(self): 
        self.name = "Dilip"
        self.__balance = 1000.0  # Private attribute

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        # You can add validation or checks here if needed
        self.__balance = new_balance

    def __private_method(self):
        print("This is a private method.")

class Employee(User): 
    def __init__(self): 
        User.__init__(self)  # Correcting the base class call
        print("Calling private member of base class: ", self.get_balance()) 
        # Accessing private attribute using getter method

obj1 = User() 
print(obj1.name) 
obj2 = Employee()

# Attempting to call the private method outside the class
# obj1.__private_method()  # This line would raise an AttributeError


"""
To ensure proper encapsulation, you should provide getter and setter methods for accessing and modifying 
private attributes. Here's how you can modify your code to use getter and setter methods:
"""

class Car:
    def __init__(self, make, model):
        self.__make = make    # Private attribute
        self.__model = model  # Private attribute

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

car1 = Car("Tata", "Indica")
print(car1.get_make())  # Accessing make using a getter method
car1.set_model("Harrier")  # Modifying model using a setter method
print(car1.get_model())  # Accessing modified model using a getter method

# =====================================================================================
class User:
    def __init__(self, username, password):
        self.__username = username  # Private attribute
        self.__password = password  # Private attribute

    def __encrypt_password(self):
        # This method would perform encryption on the password
        print("Encrypting password...")

    def get_username(self):
        # Getter method to access the username
        return self.__username

    def set_password(self, new_password):
        # Setter method to update the password
        # Here, you can add validation or encryption logic
        print("Setting new password...")
        self.__password = new_password

    def login(self, username, password):
        # Check if the provided username and password match
        if username == self.__username and password == self.__password:
            self.__encrypt_password()  # Call private method upon successful login
            print("Login successful.")
        else:
            print("Invalid username or password.")

# Example usage:
user1 = User("user123", "password123")

# Accessing private attribute using getter method
print("Username:", user1.get_username())

# Attempting to access or modify private attributes directly
# print(user1.__username)  # This line would raise an AttributeError
# user1.__password = "newpassword"  # This line would not modify the private attribute

# Proper way to update the password using the setter method
user1.set_password("newpassword123")

# Logging in with the new password
user1.login("user123", "newpassword123")

# ======================================================================================
class User:
    def __init__(self, username, password):
        self.__username = username  # Private attribute
        self.__password = password  # Private attribute
        self.__is_logged_in = False  # Private attribute

    def __encrypt_password(self):
        # This method would perform encryption on the password
        print("Encrypting password...")

    def login(self, username, password):
        # Check if the provided username and password match
        if username == self.__username and password == self.__password:
            self.__encrypt_password()  # Call private method upon successful login
            self.__is_logged_in = True
            print("Login successful.")
        else:
            print("Invalid username or password.")

    def logout(self):
        # Log out the user
        self.__is_logged_in = False
        print("Logged out successfully.")

    def is_logged_in(self):
        # Check if the user is currently logged in
        return self.__is_logged_in

# Example usage:
user1 = User("user123", "password123")

# Logging in
user1.login("user123", "password123")

# Checking if the user is logged in
print("Is user logged in?", user1.is_logged_in())

# Logging out
user1.logout()

# Checking if the user is logged in after logout
print("Is user logged in?", user1.is_logged_in())
