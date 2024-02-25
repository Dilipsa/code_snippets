"""
List is a collection data type which is ordered and mutable. Unlike Sets, Lists allow duplicate elements. 
They are useful for preserving a sequence of data and further iterating over it. 
Lists are created with square brackets.

my_list = ["Dilip", "Sapkota", "Developer"]

Creating a list
Lists are created with square brackets or the built-in list function.
# ====================================================================
list_1 = ["Dilip", "Raj", "Kumar"]
print(list_1)

# Or create an empty list with the list function
list_2 = list()
print(list_2)

# Lists allow different data types
list_3 = [5, True, "Dilip"]
print(list_3)

# Lists allow duplicates
list_4 = [0, 0, 1, 1]
print(list_4)

Access elements
# =============================================================================================================
You access the list items by referring to the index number. Note that the indices start at 0.

item = list_1[0]
print(item)

# You can also use negative indexing, e.g -1 refers to the last item,
# -2 to the second last item, and so on
item = list_1[-1]
print(item)

Change items
# =============================================================================================================
Just refer to the index number and assign a new value.

# Lists can be altered after their creation
list_1[2] = "lemon"
print(list_1)

Useful methods
# ==============================================================================================================
my_list = ["banana", "cherry", "apple"]

# len() : get the number of elements in a list
print("Length:", len(my_list))

# append() : adds an element to the end of the list
my_list.append("orange")

# insert() : adds an element at the specified position
my_list.insert(1, "blueberry")
print(my_list)

# pop() : removes and returns the item at the given position, default is the last item
item = my_list.pop()
print("Popped item: ", item)

# remove() : removes an item from the list
my_list.remove("cherry") # Value error if not in the list
print(my_list)

# clear() : removes all items from the list
my_list.clear()
print(my_list)

# reverse() : reverse the items
my_list = ["banana", "cherry", "apple"]
my_list.reverse()
print('Reversed: ', my_list)

# sort() : sort items in ascending order
my_list.sort()
print('Sorted: ', my_list)

# use sorted() to get a new list, and leave the original unaffected.
# sorted() works on any iterable type, not just lists
my_list = ["banana", "cherry", "apple"]
new_list = sorted(my_list)

# create list with repeated elements
list_with_zeros = [0] * 5
print(list_with_zeros)

# concatenation
list_concat = list_with_zeros + my_list
print(list_concat)

# convert string to list
string_to_list = list('Hello')
print(string_to_list)

Check if an item exists
# =============================================================================================================
if "banana" in list_1:
    print("yes")
else:
    print("no")

Slicing
===============================================================================================================
Access sub parts of the list wih the use of colon (:), just as with strings.

# a[start:stop:step], default step is 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a[1:3] # Note that the last index is not included
print(b)
b = a[2:] # until the end
print(b)
b = a[:3] # from beginning
print(b)
a[0:3] = [0] # replace sub-parts, you need an iterable here
print(a)
b = a[::2] # start to end with every second item
print(b)
a = a[::-1] # reverse the list with a negative step:
print(a)
b = a[:] # copy a list with slicing
print(b)

List comprehension
# =============================================================================================================
A elegant and fast way to create a new list from an existing list.

List comprehension consists of an expression followed by a for statement inside square brackets.

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i * i for i in a] # squares each element
print(b)
Output: [1, 4, 9, 16, 25, 36, 49, 64]

Nested lists
# =============================================================================================================
Lists can contain other lists (or other container types).

a = [[1, 2], [3, 4]]
print(a)
print(a[0])
"""


# Excercise:
# =============================================================================================================
data = ["Yes", "Dilip", True, 10.0, [1,2,3], 2+3j]
# To access single item, python uses indexing
print(data[0]) # Output: Yes

# To access multiple item, python uses slicing
print(data[1:3]) # Output: ['Dilip', True]

# Operations
# concatination:
lis1 = [200, 300, "Hello", True, 1000.0]
lis2 = [600, 900, "Dilip", False, 3000.0]
lis3 = ["Software Engineer",70000,3000]
print(lis1 +lis2 + lis3)

# Multiplication
lis1 = [1, 2, 3]
print(lis1*3)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]  => Repeated for 3 times

# Iteration through list:
lis1 = [100, 200, 300, 400]
for li in lis1:
  print(li+1)
'''
Output:
    101
    201
    301
    401
'''
print(lis1) # Output: [100, 200, 300, 400] => items are as it is

'''Membership of list (in and not in):'''
lis1 = ["Dilip", "Developer", 10000.0, True]
print("Dilip" in lis1)  # Output: True
print(10000.0 in lis1)  # Output: True
print(True not in lis1) # Output: False

'''using for loop'''
for li in lis1:
  if "Dilip" in lis1:
    print(f"{li} is available on the list : {lis1}")
else:
  print(f"Dilip is not available on the list : {lis1}")

# Output:
# Dilip is available on the list : ['Dilip', 'Developer', 10000.0, True]
# Developer is available on the list : ['Dilip', 'Developer', 10000.0, True]
# 10000.0 is available on the list : ['Dilip', 'Developer', 10000.0, True]
# True is available on the list : ['Dilip', 'Developer', 10000.0, True]
# Dilip is not available on the list : ['Dilip', 'Developer', 10000.0, True]
  
'''
Here we are getting multiple result because for loop is executed one by one 
and printed, but we want to print only one time, how can we do this?
Here we can create a flag called `is_available` which will be True if condition is satisfied
'''
is_available = False
for li in lis1:
  if "Dilip" in lis1:
    is_available = True
    break
  
if is_available == True:
  print(f"Dilip is available on the list : {lis1}")
else:
  print(f"Dilip is not available on the list : {lis1}")
'''is similar to'''
if is_available :
  print(f"Dilip is available on the list : {lis1}")
else:
  print(f"Dilip is not available on the list : {lis1}")
# is similar to
print(f"Dilip is available on the list : {lis1}" if is_available else f"Dilip is not available on the list : {lis1}") #ternary operator


'''Deletion of list'''
lis1 = [1,2,3,4,5]
del(lis1)
# print(lis1) #gives Error : NameError: name 'lis1' is not defined. Did you mean: `...`.? because already deleted

lis1 = [1,2,3,4,5]
print(lis1) # Output: [1, 2, 3, 4, 5],  because deletion happening in next line
del(lis1)

'''
Find length of list
By unsng python's builtin function `len()`
'''
lis = [1,2,3,4+5j, 'Good morning', [20,40,80]]
print(f"length of {lis} is {len(lis)}")   # Output : length of [1, 2, 3, (4+5j), 'Good morning', [20, 40, 80]] is 6

'''Manually:'''
count = 0
for li in lis:
  count+=1  # equals to count = count+1
print(f"length of {lis} is {count}")      # Output : length of [1, 2, 3, (4+5j), 'Good morning', [20, 40, 80]] is 6

'''
Finding maximum in list:
By usingg python's builtin function `max()`
 Syntax:
    max(iterable, key, default)

    iterable      : an iterable such as list.
    key(optional) : basis for comparision.
    default       : default value given iterable is empty.
'''
# Get largest item in a list
number = [1,2,3,7,9,8]
print(max(number))     # Output: 9

# Get largest String in a list
name = ["Dilip", "Melvin", "Rajesh", "Ram", "Susila"]
print(max(name))                # Output: Susila,  because it consider internally ASCII value of the string  
'''
# ASCII values for each element:
# Dilip : 68
# Melvin : 77
# Rajesh : 82
# Ram : 82
# Susila : 83
'''

name = ["Dilip", "Melvin", "Rajesh", "Ram", "Susila", 100]
# print(max(name))                # Output: '>' not supported between instances of 'int' and 'str', 
                                # It will not allow str and int for comparing

# using key argument
name = ["Dilip", "Melvin", "Rajesh", "Ram", "Susila"]
print(max(name, key=len))                # Output: Melvin,  Melvin is first one matched maximum charactered string  

'''
finding minimum in list
To find minimum in list, we use an inbuilt method min()
Syntax:
    min(iterable, key, default)
'''

numbers = [20, 40, 50, 60, 31, 42]
print(min(numbers))     # Output: 20

students = ["Melvin", "Raj", "Yuvaraj"]
print(min(students))   # Output: Melvin, compares ASCII value

print(min(students, key=len)) # Output: Raj, based on character length or string length

'''Default values'''
numbers = []
print(min(numbers, default=0))                     #Output: 0
print(min(numbers, default="no item in the list")) #Output: no item in the list


'''
Python  list append()
======================
The append() method adds a single item to list.
it appends an element by modifying list.
Syntax:
    list.append(item)
    item can be of any type
    it doesnot returns anything but updates existing list
'''

'''adding single item to list'''
students = ["Deepak", "Kushal", "Aayush", "Mukesh"]
print(students.append("Sudeeksha"))                 # Output: None, doesnot return
print(students)                                     # Output: ['Deepak', 'Kushal', 'Aayush', 'Mukesh', 'Sudeeksha']

''' adding multiple items one by one to list using for loop'''
# students = []
# student_numbers = int(input("How many students do you want to create a list? :"))
# for i in range(1,student_numbers+1):
#     student_name = input(f"Enter {i}{'st' if i == 1 else 'nd' if i == 2 else 'rd' if i == 3 else 'th'} student name: ") # used ternary operator
#     students.append(student_name)
  
# print(f"{student_numbers} length of students created is : {students}")

''' Finding maximum number in list without using max() function'''
numbers = [6,9,12,90,23,54,66,78,4]
max_number = numbers[0]       # just assumed 1st indexed number for comparing to all
for number in numbers:
  if number > max_number:
    max_number = number
print(max_number)             # Output: 90

'''Finding minimum number in list without using min() function'''
numbers = [6,9,12,90,23,54,66,78,4]
min_number = numbers[0]       # just assumed 1st indexed number for comparing to all
for number in numbers:            
  if number < min_number:
    min_number = number
print(min_number)             # Output : 4


'''
Python list extend()
======================
The extend() method extends a list by appending elements from an iterable.
It adds all the elements from an iterable (such as a list, tuple, or string) to the end of the list.
Syntax:
    list.extend(iterable)
    'iterable' can be a list, tuple, string, or any iterable object
    This method modifies the original list in-place and does not return a new list.
    If the 'iterable' contains multiple elements, each element is appended individually to the list.
'''

my_list = [1, 2, 3]
# Extend the list with elements from another list
my_list.extend([4, 5, 6])
print(my_list)              # Output: [1, 2, 3, 4, 5, 6]

lis_one = [1, 2, 3, 4, 5]
lis_two = [6, 7, 8, 9, 10]
lis_one.extend(lis_two)     # Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lis_one)

'''
Mostly asked interview question
What is difference between append() and extend() in list?

    append():
    The append() method adds a single element to the end of the list.
    It takes exactly one argument, which can be of any data type.
    When you call append() with an argument, that argument is added as a single element to the end of the list.
    
    Example:
        my_list = [1, 2, 3]
        my_list.append(4)
        print(my_list)  # Output: [1, 2, 3, 4]

        
    extend():
    The extend() method extends a list by appending elements from an iterable 
    (such as a list, tuple, or string) to the end of the list.
    It takes exactly one argument, which should be an iterable object.
    When you call extend() with an iterable as an argument, 
    each element from the iterable is appended individually to the end of the list.
    
    Example:
        my_list = [1, 2, 3]
        my_list.extend([4, 5, 6])
        print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

Question : How will you append multiple elements in list?
Ans      : using extend()
'''


