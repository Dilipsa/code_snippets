"""
Write a function that takes a string as input and returns a dictionary containing 
the count of each character in the string.

   Input: "hello"
   Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""
counter = 1
dic = {}
input_str="Dipinpinpinpin" #input("Enter a string:\n")
for char in input_str:
	if char != " ":
		if char not in dic:
			dic[char] = counter
		else:
			dic[char] +=counter
print(dic)
