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