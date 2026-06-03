"""
Scopes:
1. Local Scope
2. Enclosed Scope
3. Global Scope

4. Built-in Scope : If no where the variables/functions we are accessing
in the program then it will check in builtins. If not found builtins also
then it will throw error
"""

print("1. Local Scope")
print("-"*20)
# ---------------

def my_function():
    x = 10
    # This is variable x is in local scope
    # We can access This is variable x within this function only
    print("Inside my_function, value of x is :", x)

my_function()

print("#"*40, end="\n\n")
#########################
print("2. Enclosed Scope")
print("-"*20)
# ---------------

def my_outer_function():
    y = 100
    # Variable y is in enclosed scope
    # This Variable y can be accessed within this function
    #   and also nested function can access but it should use keyword
    def my_inner_function():
        nonlocal y
        print("Inside my_inner_function, value of y is :", y)
    my_inner_function()
my_outer_function()

print("#"*40, end="\n\n")
#########################
print("3. Global Scope")
print("-"*20)
# ---------------

z = 10 #  Global Scope: We can access anywhere/anyblock in the program

def my_function():
    global z
    print("Inside my_function, value of z is :", z)

my_function()

print("#"*40, end="\n\n")
#########################
