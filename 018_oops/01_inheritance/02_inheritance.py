"""
Employee Information System with Multilevel Inheritance
"""
class User:
    def __init__(self, user_name, email_address):
        self.username = user_name
        self.email = email_address

    def display_user_info(self):
        print("Username:", self.username)
        print("Email:", self.email)


class Employee(User):
    def __init__(self, username, email, employee_id):
        super().__init__(username, email)
        self.employee_id = employee_id

    def display_employee_info(self):
        super().display_user_info()  # Accessing base class method
        print("Employee ID:", self.employee_id)


# Creating an employee instance
employee1 = Employee("dilip", "dilip@example.com", "E1234")

# Accessing attributes and methods of Employee class
employee1.display_employee_info()
