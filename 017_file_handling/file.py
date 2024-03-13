"""
File handling in Python refers to the process of working with files on the file system, 
including reading from and writing to files. Python provides built-in functions and 
methods for performing various file operations. 

File Modes
====================================================================================
"r":  Read mode. Opens the file for reading.
"w":  Write mode. Opens the file for writing. If the file already exists, its contents 
      will be overwritten. If the file does not exist, a new file will be created.
"a":  Append mode. Opens the file for appending new content. If the file does not exist, 
      a new file will be created.
"b":  Binary mode. Opens the file in binary mode.
"r+": Read and Write mode. Opens the file for both reading and writing. 
      The previous data in the file can be overridden.
"w+": Write and Read mode. Opens the file for both writing and reading. 
      It will override existing data.
"a+": Append and Read mode. Opens the file for both appending and reading data. 
      It won't override existing data.

Reading from a File
====================================================================================
To read from a file, you can use methods like read(), readline(), or readlines().

# Read the entire contents of the file
content = file.read()

# Read a single line from the file
line = file.readline()

# Read all lines into a list
lines = file.readlines()


Writing to a File
====================================================================================
To write to a file, you can use the write() method.

# Open a file in write mode
file = open("dilip.txt", "w")

# Write to the file
file.write("Hello, world!\n")
file.write("This is a new line.")


Closing a File
====================================================================================
After performing file operations, it's essential to close the file using the close() 
method to free up system resources.

# Close the file
file.close()


Using a File with Context Manager
====================================================================================
Python provides a context manager (with statement) to automatically handle file closing, 
which is more efficient and safer.

# Open a file using a context manager
with open("dilip.txt", "r") as file:
    content = file.read()
    print(content)
# File is
#  automatically closed at the end of the block


Error Handling
====================================================================================
When working with files, it's essential to handle exceptions, 
such as FileNotFoundError or PermissionError.

try:
    file = open("dilip.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    if file:
        file.close()
"""
# read() gives all content from file
with open("dilip.txt", "r") as f:
  file_contents = f.read()   
  print(file_contents)

# readlines() gives all content as a list by line from file
with open("dilip.txt", "r") as f:
  file_contents = f.readlines()
  print(file_contents)
  
# gives first line content
with open("dilip.txt", "r") as f:
  file_contents = f.readline()
  print(file_contents)

# every time calling readline() gives next new line content
with open("dilip.txt", "r") as f:
  file_contents = f.readline()
  print(file_contents)


# Using for loop we can access all content line by line
with open("dilip.txt", "r") as f:
  for l in f:
    print(l, end='')

# reading amount of data
with open("dilip.txt", "r") as f:
  file_contents = f.read(20)  # reads first 20 character
  print(file_contents, end="")

  file_contents = f.read(20)  # reads next 20 character
  print(file_contents, end="")

# read all content using while loop 
with open("dilip.txt", "r") as f:
  size_to_read = 10
  file_contents = f.read(size_to_read)
  while len(file_contents) > 0:
    print(file_contents, end="*")      # added `*` to differenciate read() happened
    file_contents = f.read(size_to_read)


# To see current position
with open("dilip.txt", "r") as f:
  size_to_read = 10
  file_contents = f.read(size_to_read)
  print(file_contents)

  f.seek(0)   # to start reading at the begining at the file
  file_contents = f.read(size_to_read)
  print(file_contents)
  print(f.tell())

# Writing
with open('dilip1.txt', 'w') as f:
  f.write("Test")
  f.write("Test")  # Wrires back to back :TestTest
  f.seek(0)        # cursor takes back to start
  print(f.tell())
  f.write("R")     # Output: RestTest

# Reading from one file to writing to other file
with open('dilip.txt', 'r') as rf:
  with open('dilip_copy.txt', 'w') as wf:
    for line in rf:
      wf.write(line)


#  Reading Image file from one file to writing to other file need to open in binary mode
# with open('dilip_sapkota.png', 'rb') as rf:
#   with open('dilip_sapkota_copy.png', 'wb') as wf:
#     for line in rf:
#       wf.write(line)

# do in specific chunk sizes
with open('dilip_sapkota.png', 'rb') as rf:
  with open('dilip_sapkota_copy.png', 'wb') as wf:
    chunk_size = 1496
    rf_chunk = rf.read(chunk_size)
    while len(rf_chunk) > 0:
      wf.write(rf_chunk)
      rf_chunk = rf.read(chunk_size)