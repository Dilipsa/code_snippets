"""
Dictionary
==============================================================================================================
A dictionary is an unordered, mutable (changeable), and indexed collection. 
It is indexed by keys, which are unique and immutable objects, and each key is associated with a value.

Create a dictionary:
==============================================================================================================
my_dict = {"name":"Dilip", "age":38, "city":"Bangalore"}
print(my_dict)

or use the dict constructor, note: no quotes necessary for keys
my_dict_2 = dict(name="Raju", age=27, city="Mysore")
print(my_dict_2)


"""

"""Create a dictionary:
==============================================================================================================
"""
my_dict = {"name":"Dilip", "age":38, "city":"Bangalore"}
print(my_dict)
  # Output:
  # {"name":"Dilip", "age":38, "city":"Bangalore"}

# or use the dict constructor, note: no quotes necessary for keys
my_dict_2 = dict(name="Raju", age=27, city="Mysore")
print(my_dict_2)
  # Output:
  # {'name': 'Raju', 'age': 27, 'city': 'Mysore'}

# Access items  
name_in_dict = my_dict["name"]
print(name_in_dict)
  # Output:
  # Dilip

# Add and change items
# =================================
# add a new key
my_dict["email"] = "dilip@company.com"
print(my_dict)
  # Output:
  # {'name': 'Dilip', 'age': 38, 'city': 'Bangalore', 'email': 'dilip@company.com'}

# or overwrite the now existing key
my_dict["email"] = "dilipsapkota@nescode.com"
print(my_dict)
  # Output:
  # {'name': 'Dilip', 'age': 38, 'city': 'Bangalore', 'email': 'dilipsapkota@nescode.com'}

# Delete items
# ================================
# delete a key-value pair
del my_dict["email"]

# this returns the value and removes the key-value pair
print("popped value:", my_dict.pop("age"))
  # Output:
  # popped value: 38

# return and removes the last inserted key-value pair 
# (in versions before Python 3.7 it removes an arbitrary pair)
print("popped item:", my_dict.popitem())
  # Output:
  # popped item: ('city', 'Bangalore')

print(my_dict)
  # Output:
  # {'name': 'Dilip'}

# clear() : remove all pairs
# my_dict.clear()

# Check for keys
# ===============================
my_dict = {"name": "Deepak", "age": 28, "state": "Karnataka"}
# use if .. in ..
if "name" in my_dict:
    print(my_dict["name"])
  # Output:
  # Deepak
    
# use try except
try:
    print(my_dict["firstname"])
except KeyError:
    print("No key found") 
  # Output:
  # No key found
    
# Looping through dictionary
# ==========================
# loop over keys
# =====================================================
for key in my_dict:
    print(key, my_dict[key])
  
  # Output:
    # name Deepak
    # age 28
    # state Karnataka

# loop over keys
# ====================================================
for key in my_dict.keys():
    print(key)
  # Output
    # name
    # age
    # state

# loop over values
# ====================================================
for value in my_dict.values():
    print(value)
  # Output
    # Deepak
    # 28
    # Karnataka

# loop over keys and values
# ===================================================
for key, value in my_dict.items():
    print(key, value)
    # Output:
      # name Deepak
      # age 28
      # state Karnataka
    
# Merge two dictionaries
# ===================================================
# Use the update() method to merge 2 dicts
# existing keys are overwritten, new keys are added
my_dict = {"name":"Dilip", "age":38, "email":"dilip@company.com"}
my_dict_2 = dict(name="Sudeeksha", age=1, city="Bangalore")

my_dict.update(my_dict_2)
print(my_dict)
  # Output:
    # {'name': 'Sudeeksha', 'age': 1, 'email': 'dilip@company.com', 'city': 'Bangalore'}

# Possible key types
'''Any immutable type, like strings or numbers can be used as a key. 
Also, a tuple can be used if it contains only immutable elements.'''

# use numbers as key, but be careful
my_dict = {3: 9, 6: 36, 9:81}
# do not mistake the keys as indices of a list, e.g my_dict[0] is not possible here
print(my_dict[3], my_dict[6], my_dict[9])
  # Output:
  #   9 36 81

# use a tuple with immutable elements (e.g. number, string)
my_tuple = (8, 7)
my_dict = {my_tuple: 15}

print(my_dict[my_tuple])
  # Output:
    # 15
print(my_dict[8, 7])

# a list is not possible because it is not immutable
# this will raise an Error:
# my_list = [8, 7]
# my_dict = {my_list: 15}

# Nested dictionaries
# ============================================================================
my_dict_1 = {"name": "Dilip", "age": 38}
my_dict_2 = {"name": "Arjun", "age": 40}
nested_dict = {"dict_a": my_dict_1,
               "dictb_": my_dict_2}
print(nested_dict)
  # Output:
  #   {'dict_a': {'name': 'Dilip', 'age': 38}, 'dict_b': {'name': 'Arjun', 'age': 40}}