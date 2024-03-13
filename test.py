"""
4 pillars of OOPS
=================
1] Abstraction
2] Encapsulation
3] Inheritance
4] polymerphysm

"""

class Employee(object):
  company_name = "XYZ Company"
  no_of_employee = 0
  increment = 5

  def __init__(self, first_n, last_n, emp_id, mobile_no, emp_email, emp_salary, emp_city, emp_state, emp_country):
    self.first_name = first_n
    self.last_name = last_n
    self.employee_id = emp_id
    self.mobile = mobile_no
    self.email = emp_email
    self.salary = emp_salary
    self.city = emp_city
    self.state = emp_state
    self.country = emp_country
    Employee.no_of_employee += 1

  @property
  def name(self):
    return f"{self.first_name} {self.last_name}"

  def get_address(self):   # Instance method
    return f"city is {self.city}, state is {self.state} and country is {self.country}"
  
  def get_contact_info(self):
    return f"Mobile no is {self.mobile} and Email is {self.email}"
  
  def get_detail(self):
    return self.name, self.get_address(), self.get_contact_info()
  
  @classmethod
  def get_No_of_employee(cls):
    return cls.no_of_employee
  
  @staticmethod
  def static_method():
    return ("I am static method")
  
  @classmethod
  def set_increment(cls, inc_val):
    cls.increment = inc_val

  def __str__(self):
    return self.first_name

shiva = Employee("Shiva" ,"Kumar", "001", 888888888, "shivs@gmail.com", 10000, "Bangalore", "Karnataka", "India")
print(shiva.get_address())
print(shiva.company_name)
print(shiva.get_detail())
print(Employee.get_No_of_employee())
print(Employee.set_increment(10))
print(Employee.increment)
print(Employee.static_method())