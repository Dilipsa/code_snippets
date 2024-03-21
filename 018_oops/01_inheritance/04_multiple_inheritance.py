class User:
    def __init__(self, user_name, email_address):
        self.username = user_name
        self.email = email_address

    def display_user_info(self):
        print("Username:", self.username)
        print("Email:", self.email)


class Company:
    def __init__(self, company_name, company_address):
        self.company_name = company_name
        self.company_address = company_address

    def display_company_info(self):
        print("Company Name:", self.company_name)
        print("Company Address:", self.company_address)


class Employee(User, Company):
    def __init__(self, user_name, email_address, company_name, company_address, employee_id):
        User.__init__(self, user_name, email_address)
        Company.__init__(self, company_name, company_address)
        self.employee_id = employee_id

    def display_employee_info(self):
        self.display_user_info()
        self.display_company_info()
        print("Employee ID:", self.employee_id)


# Creating an employee instance
employee1 = Employee("dilip", "dilip@example.com", "ABC Inc.", "123 Main St", "E1234")

# Accessing attributes and methods of Employee class
employee1.display_employee_info()
