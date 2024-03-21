"""
Hierarchical inheritance:
    involves a single base class with multiple subclasses inheriting from it.
"""
class User:
    def __init__(self, user_name, email_address):
        self.username = user_name
        self.email = email_address

    def display_user_info(self):
        print("Username:", self.username)
        print("Email:", self.email)


class Company(User):
    def __init__(self, user_name, email_address, company_name, company_address):
        super().__init__(user_name, email_address)
        self.company_name = company_name
        self.company_address = company_address

    def display_company_info(self):
        super().display_user_info()
        print("Company Name:", self.company_name)
        print("Company Address:", self.company_address)


class Employee(User):
    def __init__(self, user_name, email_address, employee_id):
        super().__init__(user_name, email_address)
        self.employee_id = employee_id

    def display_employee_info(self):
        super().display_user_info()
        print("Employee ID:", self.employee_id)


class Customer(User):
    def __init__(self, user_name, email_address, customer_id):
        super().__init__(user_name, email_address)
        self.customer_id = customer_id

    def display_customer_info(self):
        super().display_user_info()
        print("Customer ID:", self.customer_id)


# Creating instances
company = Company("company_user", "company@example.com", "ABC Inc.", "123 Main St")
employee = Employee("employee_user", "employee@example.com", "E1234")
customer = Customer("customer_user", "customer@example.com", "C5678")

# Displaying information
print("--- Company Info ---")
company.display_company_info()
print("\n--- Employee Info ---")
employee.display_employee_info()
print("\n--- Customer Info ---")
customer.display_customer_info()
