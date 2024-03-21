"""
Hybrid inheritance involves a combination of multiple inheritance and hierarchical inheritance. 
It typically includes a mix of classes with multiple parent classes and subclasses inheriting from them.
"""
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


class Employee(User):
    def __init__(self, user_name, email_address, employee_id):
        super().__init__(user_name, email_address)
        self.employee_id = employee_id

    def display_employee_info(self):
        super().display_user_info()
        print("Employee ID:", self.employee_id)


class Manager(Employee, Company):
    def __init__(self, user_name, email_address, employee_id, company_name, company_address, manager_id):
        Employee.__init__(self, user_name, email_address, employee_id)
        Company.__init__(self, company_name, company_address)
        self.manager_id = manager_id

    def display_manager_info(self):
        super().display_employee_info()
        super().display_company_info()
        print("Manager ID:", self.manager_id)


# Creating an instance of Manager
manager = Manager("manager_user", "manager@example.com", "M123", "XYZ Corp.", "456 Elm St", "M456")

# Displaying manager information
manager.display_manager_info()
