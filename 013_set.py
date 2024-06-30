"""
Sets
==============================================================================================================
A Set is an unordered collection data type that is unindexed, mutable, and has no duplicate elements. 
Sets are created with curly braces {}
"""

# Create a set
# Use curly braces or the built-in set function.

my_set = {"apple", "banana", "cherry"}
print(my_set)
  # Output
  # {'banana', 'apple', 'cherry'}

# or use the set function and create from an iterable, e.g. list, tuple, string
my_set_2 = set(["one", "two", "three"])
my_set_2 = set(("one", "two", "three"))
print(my_set_2)
  # Output:
  # {'one', 'two', 'three'}

my_set_3 = set("Dilip")
print(my_set_3)
  # Output:
  # {'i', 'p', 'D', 'l'}

# careful: an empty set cannot be created with {}, as this is interpreted as dict
# use set() instead
a = {}
print(type(a))
  # Output:
    # <class 'dict'>
a = set()
print(type(a))
  # Output:
    # <class 'set'>

# Add elements
# =============================================================================================================
my_set = set()

# use the add() method to add elements
my_set.add(42)
my_set.add(True)
my_set.add("Hello")

# note: the order does not matter, and might differ when printed
print(my_set)
  # Output:
    # {True, 42, 'Hello'}

# nothing happens when the element is already present:
my_set.add(42)
print(my_set)
  # Output:
    # {True, 42, 'Hello'}

# Remove elements
# =============================================================================================================
# remove(x): removes x, raises a KeyError if element is not present
my_set = {"apple", "banana", "cherry"}
my_set.remove("apple")
print(my_set)
  # Output:
    # {'banana', 'cherry'}

# KeyError:
# my_set.remove("orange")

# discard(x): removes x, does nothing if element is not present
my_set.discard("cherry")
my_set.discard("blueberry")
print(my_set)
  # Output:
  #   {'banana'}

# clear() : remove all elements
my_set.clear()
print(my_set)
  # Output:
    # set()

# pop() : return and remove a random element
a = {True, 2, False, "hi", "hello"}
print(a.pop())
# Output:
  # False

print(a)
  # Output:
    # {True, 2, 'hi', 'hello'}

# Builtin methods
# =========================================
"""
1. add: Adds an element to the set.

  s = {1, 2, 3}
  s.add(4)
  print(s)  # Output: {1, 2, 3, 4}

2. clear: Removes all elements from the set.
  s = {1, 2, 3}
  s.clear()
  print(s)  # Output: set()

3. copy: Returns a copy of the set.
  s = {1, 2, 3}
  sc = s.copy()
  print(sc)  # Output: {1, 2, 3}

4. difference: Returns a set containing the difference between two or more sets.
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  diff = s1.difference(s2)
  print(diff)  # Output: {1, 2}

5. difference_update: Removes the items in this set that are also included in another, specified set.
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  s1.difference_update(s2)
  print(s1)  # Output: {1, 2}

6. discard: Removes the specified item from the set.
  s = {1, 2, 3}
  s.discard(2)
  print(s)  # Output: {1, 3}

7. intersection: Returns a set that is the intersection of two other sets.
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  inter = s1.intersection(s2)
  print(inter)  # Output: {2, 3}

8. intersection_update: Updates the set with the intersection of itself and another.
  s1 = {1, 2, 3}
  s2 = {2, 3, 4}
  s1.intersection_update(s2)
  print(s1)  # Output: {2, 3}

9. isdisjoint: Returns whether two sets have a null intersection.
  s1 = {1, 2, 3}
  s2 = {4, 5, 6}
  result = s1.isdisjoint(s2)
  print(result)  # Output: True

10. issubset: Returns whether another set contains this set.
  s1 = {1, 2, 3}
  s2 = {1, 2, 3, 4, 5}
  result = s1.issubset(s2)
  print(result)  # Output: True

11. issuperset: Returns whether this set contains another set.
  s1 = {1, 2, 3, 4, 5}
  s2 = {1, 2, 3}
  result = s1.issuperset(s2)
  print(result)  # Output: True

12. pop: Removes and returns an arbitrary set element.
  s = {1, 2, 3}
  element = s.pop()
  print(element)  # Output: 1 (or 2 or 3, it's arbitrary)
  print(s)  # Output: {2, 3} (or another subset depending on what was popped)

13. remove: Removes the specified element.
  s = {1, 2, 3}
  s.remove(2)
  print(s)  # Output: {1, 3}

14. symmetric_difference: Returns a set with the symmetric differences of two sets.
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  sym_diff = s1.symmetric_difference(s2)
  print(sym_diff)  # Output: {1, 2, 4, 5}

15. symmetric_difference_update: Updates a set with the symmetric difference of itself and another.
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  s1.symmetric_difference_update(s2)
  print(s1)  # Output: {1, 2, 4, 5}

16. union: Returns a set containing the union of sets.
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  uni = s1.union(s2)
  print(uni)  # Output: {1, 2, 3, 4, 5}

17. update: Updates the set with the union of itself and others.
  s1 = {1, 2, 3}
  s2 = {3, 4, 5}
  s1.update(s2)
  print(s1)  # Output: {1, 2, 3, 4, 5}

"""