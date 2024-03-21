"""
class BankAccount:
  bank_name = "ABC Bank"
  __rate_of_interest = 1.5
  def __init__(self, name, balance):
    self.name=name
    self.__balance=balance

  def set_balance(self, amt):
    self.__balance = amt
  
  def get_balance(self):
    return f"balance from get_balance(): {self.__balance} rupees."
  
  def get_interest(self):
    return f"Interest from get_interest(): {self.__get_rate_of_interest()}"
  
  def __get_rate_of_interest(self):
    return BankAccount.__rate_of_interest
  

obj = BankAccount("Melvin", 10000)
# print(obj._BankAccount__balance) # mangling

obj.__balance=20
obj.set_balance(5000)
print(obj.get_balance())
print(obj.get_interest())
print(f"balance variable from object {obj.__balance}rupees.")
"""
# def simple_gen(n):
#   for i in range(n):
#     yield i


# create a generator and function to generate a even number
# def enve_number_generator(n):
#   for i in range(n):
#     if i%2==0:
#       yield i
  
# even_no = []
# def even_number(n):
#   for i in range(n):
#     if i%2==0:
#       even_no.append(i)
#   return even_no
# import sys
# n = 1000000
# print(sys.getsizeof(enve_number_generator(n)))
# print(sys.getsizeof(even_number(n)))






# class A:
#   def greet(self,  *args):
#     print(sum(args))

# class B(A):
#   def greet(self,  *args):
#     print(sum(args))

# class C(B):
#   def greet(self, *args):
#     print(sum(args))
#   pass
# obj1 = C()
# obj1.greet(10,20,30)


"""
The ability to behave more than one form is called polymorphysm.
method overriding is an example of polymorphysm.
"""

"""
Hiding the implementation details and showing the essential features
"""

# from abc import abstractmethod, ABC
# class A(ABC):
#   @abstractmethod
#   def greet(self):
#     pass

#   @abstractmethod
#   def print_hello(self):
#     pass

#   def print_hi(self):
#     print("Hiiiiiiiiiiiiii")

# class B(A):
#   def greet(self):
#     print("good morning")

# obj = B()
# obj.greet()

"""
Abstract class is a class which has atleast one abstract method. all abstract methods 
should be implemented in sub class.
"""






# Generator
def generator_even_no(n):
  for i in range(n):
    if i%2==0:
      yield i

even_no = []
def get_even_no(n):
  for i in range(n):
    if i%2==0:
      even_no.append(i)
  return even_no


number = 1000000
even_gen = generator_even_no(number)
even = get_even_no(number)

import sys
print("using generator consumed memory in mb", sys.getsizeof(even_gen))
print("with out generator",sys.getsizeof(even))


class MyIterator:
  def __init__(self, max_value):
    self.max_value = max_value
    self.current = 0

  def __iter__(self):
    return self
  
  def __next__(self):
    if self.max_value>self.current:
      self.current += 1
      return self.current
    else:
      raise StopIteration
    
obj = MyIterator(5)
try:
  print(next(obj))
  print(obj.__next__())
  print(obj.__next__())
  print(obj.__next__())
  print(obj.__next__())
  print(obj.__next__())
except StopIteration:
  print("Item executed uccesfully")












