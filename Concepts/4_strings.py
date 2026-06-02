"""
Strings:
        - There is already a option to store name, email-id, address etc.
        - Automatically index number will be assigned to each character
"""
print("Strings PART-1")
print("How to store value")
print("-"*20)
# ---------------

a = 'PERSON'
b = "PERSON'S"
c = """PERSON'S HEIGHT IS XYZ" (" represents inch)"""
d = '''PERSON'S HEIGHT IS XYZ" (" represents inch)'''
e = 'PERSON\'S'
# \ -> represent escape character
# \ -> it will just hide next character
# \ -> will not be part of our data. our data is python's only

# In all the above cases, it will create object of builtin class
# 'str' and store values

print(a, b, c, d, e, end="\n\n")

print(a, b, c, d, e, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#########################

# ---------------
# About 'sep' argument to print() function
# ---------------
#  sep -> default value of sep is ONE SPACE
#   which means, between each value, put ONE-SPACE
# sep="\n" -> which means, between each value, put ONE-\n
#########################
print("Strings PART-2")
print("How to store value")
print("-"*20)
# ---------------

# - If there is a \ with some characters like \n\t etc
# then in string it will get replaced with newline, tab space etc.
# - This is default behavior

my_file_path_1 = "C:\newfolder\test.py"
# Automatically, \n will get replaced with newline
# \t will get replaced with tabspace
print("my_file_path_1=", my_file_path_1, end="\n\n")

my_file_path_2 = r"C:\newfolder\test.py"
# r -> raw string, it will keep characters with \, as it is.
# So, no special meaning for the characters coming with \
print("my_file_path_2=", my_file_path_2, end="\n\n")

my_file_path_3 = repr(my_file_path_1)
print("my_file_path_3=", my_file_path_3, end="\n\n")

# r -> If we want to make rawstring then we can prefix 'r'
# repr() -> string is already present, which we want to convert to raw format

print("#"*40, end="\n\n")
#########################
print("Strings PART-3")
print("How to store value")
print("-"*20)
# ---------------

x = 10
y = 20
my_string = f"Value of x is {x} and value of y is {y}"
print("my_string=", my_string, end="\n\n")
# f -> format
# f -> it will take care of replacing {variable_name} with value

print("#"*40, end="\n\n")
#########################
# ---------------
# indexing in string
# ---------------
# - Automatically index number will be assigned to every character
# - for each character there will be 2 indexes.
#   one is positive index number and other one is negative index number
# - Using index number,
#   1. Using index number, We can access SINGLE character
#   2. Using index number, We can get sub string
#   3. Using index number, We can skip characters
#   4. Using index number, We can traverse in reverse order
#########################
print("Strings PART-4")
print("1. Using index number, We can access SINGLE character")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

# Refer Example-1 in 5_strings.xlsx
print("Accessing 0th character using positive index number:", my_string[0])
print("Accessing 0th character using negative index number:", my_string[-8], end="\n\n")

# print("Accessing 100th character using positive index number:", my_string[100]) # ERROR

print("#"*40, end="\n\n")
#########################
print("Strings PART-5")
print("2. Using index number, We can get sub string")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

# Refer Example-2 in 5_strings.xlsx
print("sub string from index-1 to 6 using positive index number:",my_string[ 1 : 6 ])
print("sub string from index-1 to 6 using negative index number:",my_string[ -7 : -2 ])
print("sub string from index-1 to 6 using positive & negative index number:",my_string[ 1 : -2 ])
print("sub string from index-1 to 6 using positive & negative index number:",my_string[ -7 : 6 ], end="\n\n")

print("sub string from index-1 to END using positive index number:",my_string[ 1 :  ])
print("sub string from index-1 to END using negative index number:",my_string[ -7 :  ], end="\n\n")

print("sub string from BEGINNING to 6 using positive index number:",my_string[  : 6 ])
print("sub string from BEGINNING to 6 using negative index number:",my_string[  : -2 ], end="\n\n")

# IMPORTANT: In slicing, always character specified in end index will not
# be-coming/not-included/excluded in substring. Which means
# character at index-6 will be excluded

print("#"*40, end="\n\n")
#########################
print("Strings PART-6")
print("3. Using index number, We can skip characters")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

# Refer Example-3 in 5_strings.xlsx
print("sub string from index-1 to 6 using positive index number with default step value=1:",my_string[ 1 : 6 ])
print("sub string from index-1 to 6 using negative index number with default step value=1:",my_string[ -7 : -2 ], end="\n\n")
# default step value=1: Which means, from index-1 to 6, give me every character

print("sub string from index-1 to 6 using positive index number with step value=1:",my_string[ 1 : 6 : 1 ])
print("sub string from index-1 to 6 using negative index number with step value=1:",my_string[ -7 : -2 : 1 ], end="\n\n")
# step value=1: Which means, from index-1 to 6, give me every character

print("sub string from index-1 to 6 using positive index number with step value=2:",my_string[ 1 : 6 : 2 ])
print("sub string from index-1 to 6 using negative index number with step value=2:",my_string[ -7 : -2 : 2 ], end="\n\n")
# step value=2: Which means, from index-1 to 6, give me every 2nd character

print("sub string from index-1 to 6 using positive index number with step value=3:",my_string[ 1 : 6 : 3 ])
print("sub string from index-1 to 6 using negative index number with step value=3:",my_string[ -7 : -2 : 3 ], end="\n\n")
# step value=3: Which means, from index-1 to 6, give me every 3rd character

print("#"*40, end="\n\n")
#########################
print("Strings PART-7")
print("4. Using index number, We can traverse in reverse order")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

# Refer Example-4 in 5_strings.xlsx

# Example to understand reverse order
# Example: index-6 to 1 in reverse direction
# MANDATORY 3 STEPS:
# Step-1: Start index should be 6
# Step-2: End index should be 1
# Step-3: Step value should be negative value. Here it is -1
# IMPORTANT: If we miss any step then we will get EMPTY string

print("sub string from index-6 to 1 in reverse order, using positive index number with step value = -1:", my_string[ 6 : 1 : -1 ])
print("sub string from index-6 to 1 in reverse order, using negative index number with step value = -1:", my_string[ -2 : -7 : -1 ], end="\n\n")
# Step value = -1: Which mens, from index 6 to 1, give me every character, reverse order

print("sub string from index-6 to 1 in reverse order, using positive index number with step value = -2:", my_string[ 6 : 1 : -2 ])
print("sub string from index-6 to 1 in reverse order, using negative index number with step value = -2:", my_string[ -2 : -7 : -2 ], end="\n\n")
# Step value = -2: Which mens, from index 6 to 1, give me every 2nd character, reverse order

print("#"*40, end="\n\n")
#########################
print("Strings PART-8")
print("METHODS is present inside 'str' class")
print("-"*20)
# ---------------

print(dir(str))

print("#"*40, end="\n\n")
#########################

print("Strings PART-9")
print("Creating 2 objects with some value")
print("-"*20)
# ---------------

object_1 = "Hi"
# Internally it will create object of 'str' class and store value
object_2 = "Hello"
# Internally it will create object of 'str' class and store value

print("#"*40, end="\n\n")
#########################

print("Strings PART-10")
print("Values present in both objects")
print("-"*20)
# ---------------

print(object_1)
print(object_2)

print("#"*40, end="\n\n")
#########################

print("Strings PART-11")
print("One copy of the methods going to both objects")
print("-"*20)
# ---------------

print("One copy of the METHODS present inside object_1:", dir(object_1), sep="\n", end="\n\n")
print("One copy of the METHODS present inside object_2:", dir(object_2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Strings PART-12")
print("Capitalize() method")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

capitalized_my_string = my_string.capitalize() #
print("capitalized_my_string=", capitalized_my_string, end="\n\n")

print("#"*40, end="\n\n")
#########################
print("Strings PART-13")
print("find() method")
print("-"*20)
# ---------------

my_string = "WEL COME"
print("my_string=", my_string, end="\n\n")

# Feature-1
index_of_first_E = my_string.find("E") # Returns index of 1st occurrance of E
print("index_of_first_E=", index_of_first_E, end="\n\n")

# Feature-2
index_of_next_E = my_string.find("E", 4) # start from index-4
print("index_of_next_E=", index_of_next_E, end="\n\n")

# Feature-3
index_of_COME = my_string.find("COME") # Returns index of 'C'
print("index_of_COME=", index_of_COME, end="\n\n")

# Feature-4
index_of_XYZ = my_string.find("XYZ") # Returns -1 if not found
print("index_of_XYZ=", index_of_XYZ, end="\n\n")

print("#"*40, end="\n\n")
#########################
