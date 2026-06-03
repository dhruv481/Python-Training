"""
How to store data inside each object

2 ways:
1-way: we can store data without using methods
2-way: we can store data through methods

In this section,
1-way: we can store data without using methods
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

print("Store DATA inside each object")
print("-"*20)
# ---------------

Employee.company_name = "XYZ Company"
# Inside 'Employee' object/cubicle,
# It will create one variable called company_name
# and store value
Employee.company_location = "XYZ Location"
# Inside 'Employee' object/cubicle,
# It will create one variable called company_location
# and store value

# So, finally, inside object/cubicle 'Employee', we have 2 variables

e1.name = "emp-1"
# Inside 'e1' object/cubicle,
# It will create one variable called name
# and store value
e1.email = "emp-1@someemail"
# Inside 'e2' object/cubicle,
# It will create one variable called email
# and store value

# So, finally, inside object/cubicle 'e1', we have 2 variables i.e. name, email

e2.name = "emp-2"
# Inside 'e2' object/cubicle,
# It will create one variable called name
# and store value
e2.email = "emp-2@someemail"
# Inside 'e2' object/cubicle,
# It will create one variable called email
# and store value
e2.phone = 123456
# Inside 'e2' object/cubicle,
# It will create one variable called phone
# and store value

# So, finally, inside object/cubicle 'e2', we have 3 variables i.e. name, email, phone

print("#"*40, end="\n\n")
#########################

print("Access DATA inside each object")
print("-"*20)
# ---------------

print("Company Name:", Employee.company_name)
print("Company Location:", Employee.company_location, end="\n\n")

print("Employee 1 Name:", e1.name)
print("Employee 1 Email:", e1.email, end="\n\n")

print("Employee 2 Name:", e2.name)
print("Employee 2 Email:", e2.email)
print("Employee 2 Phone:", e2.phone, end="\n\n")

print("#"*40, end="\n\n")
#########################