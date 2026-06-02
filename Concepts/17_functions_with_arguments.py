"""
In this program, we are discussing on,
Case-2: How to pass values to variables present inside the function?

4 ways we can pass values to function
1-way: positional arguments
    - While calling the function, we need to specify only VALUES to argument
2-way: keyword arguments
    - While calling the function, we need to specify
        both ARGUMENT NAME and VALUES to argument
3-way: variable positional arguments
    - While calling the function, for ONLY ONE ARGUMENT in the function definition,
        we can pass 0 or more VALUES
4-way: variable keyword arguments
    - While calling the function, for ONLY ONE ARGUMENT in the function definition,
        we can pass 0 or more both ARGUMENT NAME and VALUES
"""

print("""1-way: positional arguments.
    - While calling the function, we need to specify only VALUES to argument""")
print("-"*20)
# ---------------

# / -> / is just syntax to tell it is positional argument
# / -> / is not counted as an argument. So, below
#       function is taking 2 arguments only i.e, name and company

#  name and company are called positional arguments
# where while calling the function, we can pass only values to those arguments

def employee(name, company, /):
    return {"name": name, "company": company}

received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################
print("""2-way: keyword arguments
    - While calling the function, we need to specify
        both ARGUMENT NAME and VALUES to argument""")
print("-"*20)
# ---------------

# * -> * is just syntax to tell it is keyword argument
# * -> * is not counted as an argument. So, below
#       function is taking 2 arguments only i.e, name and company

#  name and company are called keyword arguments
# where while calling the function, we can pass BOTH ARGUMENT NAME and VALUES
# to those arguments

def employee(*, name, company):
    return {"name": name, "company": company}

received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
#########################
print("""3-way: variable positional arguments
    - While calling the function, for ONLY ONE ARGUMENT in the function definition,
        we can pass 0 or more VALUES""")
print("-"*20)
# ---------------

# *a : called variable positional arguments
#       where it can receive 0 or more values

def my_add_function(*a):
    print("Received all values passed to this function and keeping in TUPLE:", a)

my_add_function()
my_add_function(10, 20, 30, 40, 50)

print("#"*40, end="\n\n")
#########################
print("""4-way: variable keyword arguments
    - While calling the function, for ONLY ONE ARGUMENT in the function definition,
        we can pass 0 or more both ARGUMENT NAME and VALUES""")
print("-"*20)
# ---------------

# **employee_details : Variable keyword arguments
#     - While calling the function, for ONLY ONE ARGUMENT in the function definition,
#         we can pass 0 or more both ARGUMENT NAME and VALUES

def employee_db_update(**employee_details):
    print("""Received BOTH ARGUMENT NAME and  VALUES passed to this function
    and keeping in DICTIONARY:""", employee_details)

employee_db_update()
employee_db_update(name="emp-1", company="comp-1")
employee_db_update(name="emp-2", company="comp-2", phone=12345, email="e1@email.com")

print("#"*40, end="\n\n")
#########################