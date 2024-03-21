class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_user_info(self):
        print("Username:", self.username)
        print("Email:", self.email)


class Company(User):
    def __init__(self, username, email, company_name):
        super().__init__(username, email)
        self.company_name = company_name

    def display_company_info(self):
        self.display_user_info()  # Accessing base class method
        print("Company Name:", self.company_name)


class Employee(Company):
    def __init__(self, username, email, company_name, employee_id):
        super().__init__(username, email, company_name)
        self.employee_id = employee_id

    def display_employee_info(self):
        self.display_company_info()  # Accessing intermediate class method
        print("Employee ID:", self.employee_id)


# Creating an employee instance
employee1 = Employee("dilip", "dilip@example.com", "XYZ Inc.", "E1234")

# Accessing attributes and methods of Employee class
employee1.display_employee_info()
