"""
Why object

In this section, 2 terminologies.
Encapsulation: Keeping DATA and METHODS together
Abstraction:
    - Why methods present inside each class?
    - Idea is, we will develop all the functionalities
    and release class to end user. End user will
    just know what each method is doing and
    end user will use that method. end user no need
    to know how each method is implemented OR
    writing methods inside the class to provide abstraction
    to end user
"""
print("METHODS is present inside 'str' class")
print("-"*20)
# ---------------

print(dir(str))

print("#"*40, end="\n\n")
#########################

print("Creating 2 objects with some value")
print("-"*20)
# ---------------

object_1 = "Hi"
# Internally it will create object of 'str' class and store value
object_2 = "Hello"
# Internally it will create object of 'str' class and store value

print("#"*40, end="\n\n")
#########################

print("DATA present in both objects")
print("-"*20)
# ---------------

print(object_1)
print(object_2)

print("#"*40, end="\n\n")
#########################

print("One copy of the methods going to both objects")
print("-"*20)
# ---------------

print("One copy of the METHODS present inside object_1:", dir(object_1), sep="\n", end="\n\n")
print("One copy of the METHODS present inside object_2:", dir(object_2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#########################