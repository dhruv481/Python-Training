"""
About __ double underscore names
1. These __ double underscore names are system defined names
2. Few __ double underscore names are used in methods defined in 'object' class
    like
    __new__()
    __init__()
3. Few __ double underscore names are used for operators
    like __add__ for +
4. Few __ double underscore names are used in builtin functions
    like __len__ for len()
"""

print("Overriding init method")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, name): # self=e1, "emp-1"
        self.name = name
    def get_name(self):
        return self.name

e1 = Employee("emp-1") # __init__("emp-1")
# When we create object, internally it will execute 2 methods
#   1) __new__() which will construct the object
#   2) __init__() which will initialize the object
# ANY method which is coming from super class can be rewritten.
# This is called method OVERRIDING. We can use same method name
# as super class method name. This is called POLYMORPHISM
print("Employee name:", e1.get_name())


print("#"*40, end="\n\n")
#########################
print("Supporting + operator")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, name): # self=e1, "emp-1"
        self.name = name
    def get_name(self):
        return self.name
    def __add__(self, second_object): # self=e1, second_object = e2
        concat_result = self.name + second_object.name
        return concat_result

e1 = Employee("emp-1")
print("Employee name:", e1.get_name())

e2 = Employee("emp-2")
print("Employee name:", e2.get_name(), end="\n\n")

result = e1 + e2 # __add__(e1, e2)
print("Add Result:", result, end="\n\n")

print("#"*40, end="\n\n")
#########################
print("Supporting len() function")
print("-"*20)
# ---------------

class Employee:
    def __init__(self, name): # self=e1, "emp-1"
        self.name = name
    def get_name(self):
        return self.name
    def __add__(self, second_object): # self=e1, second_object = e2
        concat_result = self.name + second_object.name
        return concat_result
    def __len__(self): # self = e1 or e2
        return len(self.name)


e1 = Employee("emp-1")
print("Employee 1 name:", e1.get_name())

e2 = Employee("emp-200")
print("Employee 2 name:", e2.get_name(), end="\n\n")

result = e1 + e2 # __add__(e1, e2)
print("Add Result:", result, end="\n\n")

print("Length of e1:", len(e1)) # e1.__len__()
print("Length of e2:", len(e2), end="\n\n")

print("#"*40, end="\n\n")
#########################

# ---------------
# Documentation:
# ---------------
# https://docs.python.org/3/reference/datamodel.html#special-method-names
#########################
