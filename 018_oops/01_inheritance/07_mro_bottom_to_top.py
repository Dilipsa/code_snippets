"""
To implement Method Resolution Order (MRO) from bottom to top, we need to carefully design the class hierarchy 
and method calls so that each class's methods are called explicitly without relying on super() to traverse 
the inheritance chain. Here's an example demonstrating this:
"""
class User:
    def __init__(self, user_name, email_address):
        self.username = user_name
        self.email = email_address

    def display_info(self):
        print("User Info:")
        print("Username:", self.username)
        print("Email:", self.email)


class Employee(User):
    def __init__(self, user_name, email_address, employee_id):
        super().__init__(user_name, email_address)
        self.employee_id = employee_id

    def display_info(self):
        print("Employee Info:")
        super().display_info()
        print("Employee ID:", self.employee_id)


class Company(Employee):
    def __init__(self, user_name, email_address, company_name, company_address):
        super().__init__(user_name, email_address, "Employee ID123")
        self.company_name = company_name
        self.company_address = company_address

    def display_info(self):
        print("Company Info:")
        super().display_info()
        print("Company Name:", self.company_name)
        print("Company Address:", self.company_address)


class Manager(Company):
    def __init__(self, user_name, email_address, company_name, company_address, manager_id):
        super().__init__(user_name, email_address, company_name, company_address)
        self.manager_id = manager_id

    def display_info(self):
        print("Manager Info:")
        super().display_info()
        print("Manager ID:", self.manager_id)


# Creating an instance of Manager
manager = Manager("manager_user", "manager@example.com", "XYZ Corp.", "123 Main St", "M456")

# Accessing the method
manager.display_info()

# Accessing the attributes
print("Accessing username:", manager.username)
print("Accessing email:", manager.email)


print("MRO for User:", User.mro())
print("MRO for Employee:", Employee.mro())
print("MRO for Company:", Company.mro())
print("MRO for Manager:", Manager.mro())