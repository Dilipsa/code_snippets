"""
Strings
#============================================
Strings are used in Python to record text information, such as names. 
Strings in Python are actually a sequence, which basically means Python keeps track of 
every element in the string as a sequence. 

For example: 
  Python understands the string "hello' to be a sequence of letters in a specific order. 
  This means we will be able to use indexing to grab particular 
  letters (like the first letter, or the last letter).


Creating Strings
# =============================================
Strings in Python can be created using single quotes or double quotes or even triple quotes.

# with single Quotes 
String1 = 'Welcome to the the tutorial'

# with double Quotes 
String1 = "I'm a Dilip"

# with triple Quotes 
String1 = '''I'm a Dilip Sapkota and I  am a django developer'''

# Quotes allows multiple lines 
String1 = '''Welcome 
            To the 
            Tutorial'''

Accessing characters in Python String
# ==========================================
In Python, individual characters of a String can be accessed by using the method of Indexing. 
Index number always starts from 0(zero).

Indexing allows negative address references to access characters from the back of the String, 
e.g. -1 refers to the last character, -2 refers to the second last character, and so on. 

String1 = "Dilip"
print(String1)     => prints `Dilip`
  
print(String1[0])  => prints `D` 

print(String1[-1]) => prints `p`


String Slicing
#==========================================
extracting a portion (substring) of a string is called slicing
print(String1)  # Output: Dilip

Slicing in Python is a technique used to extract a portion of a string, 
list, or any other sequence-like data structure. 

Syntax for slicing
string[start:end:step]

Example:
  dilip_string = "Dilip"
  # Extracting the first three characters
  print(dilip_string[:3])  # Output: "Dil"

  # Extracting the last two characters
  print(dilip_string[-2:]) # Output: "ip"

  # Reversing the string
  print(dilip_string[::-1]) # Output: "piliD"


"""

greet = 'Good Afternoon'
greet = "Good Morning"
greet = '''Good Evening'''
greet = """Good Night"""

# info = 'Hello I'm Dilip'  # to avoid error we can surround the string with double quote 
info = "Hello I'm Dilip"
info = 'Hello I\'m Dilip' 

letters = "A\tB\nC\tD"
directory = r"c:\\users\tabular_data\new\info"

info = 'Lorem Ipsum is simply dummy text of the printing and\
typesetting industry. Lorem Ipsum has been the industry\'s\
standard dummy text ever since the 1500s, when an unknown\
printer took a galley of type and scrambled it\
to make a type  specimen book. It has survived not\
only five centuries,  but also the leap into electronic\
ypesetting, remaining\
essentially unchanged. It was popularised in the 1960s with\
the release of Letraset sheets containing Lorem Ipsum passages,\
and more recently with desktop publishing software like Aldus\
PageMaker including versions of Lorem Ipsum.'

name = "Dilip Sapkota"
# slicing:
# string[start:end:step]
print(name[0]) 
print(name[2]) 

print(name[1:])  # gives everything from 1st index character to last
print(name[:12]) # gives character from oth index to 11th indexed character
print(name[::3]) # gices all character with step of third index
print(name[2:8]) # gives character of 2nd index number to 7th index character
print(name[0:4:2]) # gives every second character from 0th index number to 3rd index number
print(name[0:10:3]) # gives every third character from 0th index number to 9th index number
print(name[::])     #Prints everything

print(name[-1])  #gives last index numbered character
print(name[-3])  #gives third last index numbered character

print(name[-9:-1]) # `p Sapkot` > from -9th indexed character to second last indexed character
print(name[-10:-1:2])

print(name[::-1])   # Reverses the String

# print(dir(name))  # gives all methodes available for string
# print(help(str))  #Explain about the functionality
# Some Useful String methods
greet = "Good morning"
print(greet.upper())
print(greet.title())
print(greet.lower())
print(len(greet))

info = "       my name is Dilip Sapkota    "
print(info.strip())
info = "my*na* me*is* : Dilip* Sapkota"

list_info = info.split()
print(list_info)


# Taking Input From User
# your_name = "Dilip"
your_name = input("Enter your name:")
greet = "Good Morning"

# print("Hello", greet, your_name)
print(("Hello {} {}").format(your_name, greet))
      
print(f"Hello {your_name} {greet}.")

"""
1. capitalize()
  s = "hello"
  print(s.capitalize())  # Output: "Hello"

2. casefold()
  s = "Hello"
  print(s.casefold())  # Output: "hello"

3. center()
  s = "hello"
  print(s.center(10))  # Output: "  hello   "

4. count()
  s = "hello world"
  print(s.count('o'))  # Output: 2

5. encode()
  s = "hello"
  print(s.encode())  # Output: b'hello'

6. endswith()
  s = "hello"
  print(s.endswith('lo'))  # Output: True

7. expandtabs()
  s = "hello\tworld"
  print(s.expandtabs(4))  # Output: "hello   world"

8. find()
  s = "hello"
  print(s.find('e'))  # Output: 1

9. format()
  s = "Hello, {}"
  print(s.format("world"))  # Output: "Hello, world"

10. format_map()
  s = "Hello, {name}"
  print(s.format_map({"name": "world"}))  # Output: "Hello, world"

11. index()
  s = "hello"
  print(s.index('e'))  # Output: 1

12. isalnum()
  s = "hello123"
  print(s.isalnum())  # Output: True

13. isalpha()
  s = "hello"
  print(s.isalpha())  # Output: True

14. isascii()
  s = "hello"
  print(s.isascii())  # Output: True

15. isdecimal()
  s = "12345"
  print(s.isdecimal())  # Output: True

16. isdigit()
  s = "12345"
  print(s.isdigit())  # Output: True

17. isidentifier()
  s = "variable_name"
  print(s.isidentifier())  # Output: True

18. islower()
  s = "hello"
  print(s.islower())  # Output: True

19. isnumeric()
  s = "12345"
  print(s.isnumeric())  # Output: True

20. isprintable()
  s = "hello"
  print(s.isprintable())  # Output: True

21. isspace()
  s = "   "
  print(s.isspace())  # Output: True

22. istitle()
  s = "Hello World"
  print(s.istitle())  # Output: True

23. isupper()
  s = "HELLO"
  print(s.isupper())  # Output: True

24. join()
  s = "-"
  print(s.join(["hello", "world"]))  # Output: "hello-world"

25. ljust()
  s = "hello"
  print(s.ljust(10))  # Output: "hello     "

26. lower()
  s = "HELLO"
  print(s.lower())  # Output: "hello"

27. lstrip()
  s = "   hello"
  print(s.lstrip())  # Output: "hello"

28. maketrans()
  s = "hello"
  trans = s.maketrans("h", "j")
  print(s.translate(trans))  # Output: "jello"

29. partition()
  s = "hello world"
  print(s.partition(" "))  # Output: ('hello', ' ', 'world')

30. removeprefix()
  s = "hello world"
  print(s.removeprefix("hello"))  # Output: " world"

31. removesuffix()
  s = "hello world"
  print(s.removesuffix("world"))  # Output: "hello "

32. replace()
  s = "hello world"
  print(s.replace("world", "Python"))  # Output: "hello Python"

33. rfind()
  s = "hello world"
  print(s.rfind('o'))  # Output: 7

34. rindex()
  s = "hello world"
  print(s.rindex('o'))  # Output: 7

35. rjust()
  s = "hello"
  print(s.rjust(10))  # Output: "     hello"

36. rpartition()
  s = "hello world"
  print(s.rpartition(" "))  # Output: ('hello', ' ', 'world')

37. rsplit()
  s = "hello world"
  print(s.rsplit())  # Output: ['hello', 'world']

38. rstrip()
  s = "hello   "
  print(s.rstrip())  # Output: "hello"

39. split()
  s = "hello world"
  print(s.split())  # Output: ['hello', 'world']

40. splitlines()
  s = "hello\nworld"
  print(s.splitlines())  # Output: ['hello', 'world']

41. startswith()
  s = "hello"
  print(s.startswith("he"))  # Output: True

42. strip()
  s = "   hello   "
  print(s.strip())  # Output: "hello"

43. swapcase()
  s = "Hello World"
  print(s.swapcase())  # Output: "hELLO wORLD"

44. title()
  s = "hello world"
  print(s.title())  # Output: "Hello World"

45. translate()
  s = "hello"
  trans = str.maketrans("h", "j")
  print(s.translate(trans))  # Output: "jello"

46. upper()
  s = "hello"
  print(s.upper())  # Output: "HELLO"

47. zfill()
  s = "hello"
  print(s.upper())  # Output: "HELLO"
"""