"""
Strings
#============================================
Strings are used in Python to record text information, such as names. 
Strings in Python are actually a sequence, which basically means Python keeps track of 
every element in the string as a sequence. For example, 
Python understands the string "hello' to be a sequence of letters in a specific order. 
This means we will be able to use indexing to grab particular 
letters (like the first letter, or the last letter).


1.) Creating Strings
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

#Accessing characters in Python String
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
print(String1)  # Output: World


"""