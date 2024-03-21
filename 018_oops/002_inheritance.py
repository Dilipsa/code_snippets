"""
# Inheritance
=================================================================================================
Inheritance is a process by which we can access one class properties to another class.
A class which is extended by other class is called super class / parent class / base class.
A class which extends another classs is called extended class / child class / inherited class / derived class.
types of Inheritance:
1] Single inheritance       : One parent class is extended/inherited by another child class.
2] Multiple inheritance     : Multiple parent class extended by a class.
3] Multi level inheritance  : Level of inheritance is more than one, class Grandfather is extended.
                              by class Father and Father class is extended by child class.
4] Hierarchical inheritance : One parent class is extended by more than one child classs.
5] Hybrid inheritance       : Mix of all types of inheritance. 
"""

class User:
  def __init__(self, f_name):
    self.first_name = f_name

  def get_info(self):
    return f"First name is {self.first_name}"
  
  def __str__(self):
    return self.first_name

class Employee(User):
  def __init__(self,  f_name, emp_id):
    super().__init__(f_name)
    self.employee_id = emp_id
  
  def get_info(self):
    return "Hello Employee"

class Department(Employee):
  def __init__(self, f_name, emp_id, dept_name):
    self.department = dept_name
    super().__init__(f_name, emp_id)

  def get_info(self):
    return "Hello production"

melvin = Department("Melvin", "emp_001", "Designing")


print(melvin.get_info())

