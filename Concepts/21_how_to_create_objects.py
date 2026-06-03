"""
How to create objects?
- Using class we can create n number of objects

In this section, 2 terminologies
1. Class Object
2. Instance Object
"""
print("Writing our own class")
print("-"*20)
# ---------------

class Employee:
    pass

print("#"*40, end="\n\n")
#########################

# ---------------
# About 'pass' keyword
# ---------------
# - 'pass' keyword is DUMMY keyword
# - DUMMY keyword means, if we execute nothing will happen
# - Use 'pass' keyword to keep any block empty like if-block, for-block
#########################

# ---------------
# About 'Employee' class
# ---------------
# - 'Employee' class is empty class
# - Even though 'Employee' class is EMPTY, it is VALID class
# - VALID class means,
#      -- We can create n number of objects
#       -- We can store DATA inside each objects
#       -- Since class is empty, NO METHODS present in each object
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

# ---------------
# Total we have 3 objects
# ---------------
# 1. Class Object: In the name of the class 'Employee' one object is
#       automatically getting created
# 2. Instance Object: Which we created i.e, e1 & e2
#
# NOTE:
# - we can use all 3 objects to keep DATA and METHODS
# - We are using class object to keep DATA and METHODS which is common
#   for all instance objects
#########################