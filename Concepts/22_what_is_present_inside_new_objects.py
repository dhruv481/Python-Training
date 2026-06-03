"""
Check what is present in each new object.
"""
print("Writing our own class")
print("-"*20)
# ---------------

class Employee:
    pass

print("#"*40, end="\n\n")
#########################

print("Creating 2 objects")
print("-"*20)
# ---------------

e1 = Employee()
# It will create new object and name it as e1. e1 is called reference
e2 = Employee()
# It will create new object and name it as e2. e2 is called reference

print("#"*40, end="\n\n")
#########################

print("METHODS present in each new object")
print("-"*20)
# ---------------

print("METHODS present inside brand new class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS present inside brand new instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS present inside brand new instance object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#########################

# ---------------
# About 1st class in python 'object' class
# ---------------
# - 'object' class is 1st class in python
#
# - 'object' class will be having basic methods which is
#   required for each and every class
#   like
#   __new__() # Constructor # This will construct the object
#   __init__() # Initializer # This will initialize the object
#
# - When we write new class, internally, automatically,
#   whatever there in 'object' class will come to
#   new class. This is also called as INHERITANCE
#########################