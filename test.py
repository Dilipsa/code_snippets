"""num = 10
if num == 10:
  print("this is 10")
elif num == 20:
  print("this is 20")
elif num == 30:
  print("this is 30")
else:
  print("something else")

if num == 10:
  print("this is 10")
if num == 20:
  print("this is 20")


if num == 30:
  print("this is 30")
else:
  print("something else")

# Some common scenario
name = "Dilip"
name = None
name = "None"
name = ""
name = 0
name = -1
name = "0"
name = int("0")

if name:
  print("If part")
else:
  print("Else part")
print(not name)
print(name is None)
print(name is not None)


'''Ternary operator or single line if else statement'''

print("If part" if name else "Else part")

num = [10,20,30]
print("30 available in the list" if 30 in num else "30 is not available in the list")

print(30 not in num)

'''understand the difference between `==` and `is` '''
a = 20
b = 20

print(a==b)
print(a is b)
print(f" id of {a} is {id(a)}")
print(f" id of {b} is {id(b)}")

l1 = [1,2,3]
l2 = [1,2,3]

print(l1 == l2)
print(l1 is l2)
print(f" id of {l1} is {id(l1)}")
print(f" id of {l2} is {id(l2)}")

'''simple example of for else loop'''
for i in range(1,11):
  if i == 5:
    continue
  print(i)
else:
  print("I am executed")


lis = [1,2,3,4,5,6,7,8,9,10]
even_lis = []

for l in lis:
  if l%2 == 0:
    even_lis.append(l)
  print(even_lis)
    
# functions
def get_info(*args, **kwargs):
  sum = 0
  for i in args:
    sum = sum+i
  print(sum)
  for key, value in kwargs.items():
    print(key, value)

dic = {'num1':10, 'num2':20, 'num3':40}
tup = [10, 20, 30, 40]
get_info(*tup, **dic) 

'''lambda functions'''
# defined function / named function / normal function
def square(n):
  return n**2

# lambda function / ananomous function / nameless function
l = lambda n:n**2
print(l(6))

# map(), filter() and reduce() functions with lambda
print(list(map(lambda n:"vandana", (1,2,3,4,5))))
[1, 4, 9, 16, 25]

even_no = list(map(lambda x :x**2==0, [0, 1,2,3,4,5,6,7,8,10]))
print(even_no)

from functools import reduce
sum = reduce(lambda x,y:x+y, [1,2,3,4,5,6])
print(sum)

#  without reduce function
sum = 0
def find_sum(*args):
  global sum
  for i in args:
    sum = sum+i
find_sum(1,2,3,4,5,6)
print(sum)

# list comprehension

l = [1,2,3,4,5,6,7,8,9,10]
print([i for i in l if i<5]) # list comprehension

#  using for loop
even_no = []
for i in l:
  if i%2==0:
    even_no.append(i)
print(even_no)
"""


# def decorator(grt):
#   def inner(*args, **kwargs):
#     result = grt(*args, **kwargs)
#     num3 = int(input("Enter a number to add from decorator:\n"))
#     return result + num3
#   return inner

# @decorator
# def add_num(num1, num2):
#   return num1+num2
# print(add_num(20,30))


# def decorator(func):
#   def inner(*args):
#     result = func(*args)
#     length = len(args)
#     avg = result / length
#     print(result)
#     return avg
#   return inner

# @decorator
# def find_sum(num1, num2):
#   return num1+num2
# print(find_sum(10,20))

# def add_nums(*args):
#   from functools import reduce
#   print(reduce(lambda x,y:x+y, args))
#   # print(num1+num2)

# add_nums(10,20)

# create a function which returns the sum of 
# numbers without using sum(), use *args
# numbers = (1,2,3,5)
# for num in numbers:
#   num+=num
# print(num)

# try:
#   num_one = 10 #int(input("Enter your first number:"))
#   num_two = '0' #int(input("Enter your second number:"))
#   print(num_one / num_two)

# except ZeroDivisionError as e:
#   print("I am inside Except block", e)    # This will be executed when an exception occured in try block
# except FileNotFoundError as e:
#   print(e)
# else:
#   print("I will be executed if there is no exception occured")      # This will be executed if try block executed successfully
# finally:
#   print("I will be executed any time whether any exception occurs or not.")
