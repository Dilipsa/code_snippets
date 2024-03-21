"""
Multiple inheritance in Python follows a specific method resolution order (MRO) that is typically from left to right. 
This means that when a class inherits from multiple parent classes, the order in which those parent classes are listed 
determines the order in which their methods are searched for and executed.
"""
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        print("User Info:")
        print("Username:", self.username)
        print("Email:", self.email)


class Employee(User):
    def __init__(self, username, email, employee_id, company_name, company_address):
        super().__init__(username, email)
        self.employee_id = employee_id
        self.company_name = company_name
        self.company_address = company_address

    def display_info(self):
        print("Employee Info:")
        super().display_info()  # Call method from User class
        print("Employee ID:", self.employee_id)
        print("Company Name:", self.company_name)
        print("Company Address:", self.company_address)


class Company:
    def __init__(self, company_name, company_address):
        self.company_name = company_name
        self.company_address = company_address

    def display_info(self):
        print("Company Info:")
        print("Company Name:", self.company_name)
        print("Company Address:", self.company_address)


class Manager(Employee, Company):
    def __init__(self, username, email, company_name, company_address, employee_id, manager_id):
        Employee.__init__(self, username, email, employee_id, company_name, company_address)
        Company.__init__(self, company_name, company_address)
        self.manager_id = manager_id

    def display_info(self):
        print("Manager Info:")
        super().display_info()  # Call display_info from Employee
        print("Manager ID:", self.manager_id)


# Creating an instance of Manager
manager = Manager("manager_user", "manager@example.com", "XYZ Corp.", "123 Main St, Bangalore", "E1234", "M456")

# Accessing the method
manager.display_info()

# Accessing the attributes
print("Accessing username:", manager.username)
print("Accessing email:", manager.email)

print("MRO for User:", User.mro())
print("MRO for Employee:", Employee.mro())
print("MRO for Company:", Company.mro())
print("MRO for Manager:", Manager.mro())