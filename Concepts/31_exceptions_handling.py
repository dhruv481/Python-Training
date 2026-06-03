"""
Exceptions Handling: When we run the program, if any line is throwing error
then program will terminate abruptly on that line only. We can avoid/take-care of
this abruptly termination using exceptions handling
"""
# print("WITHOUT handling exceptions")
# print("-"*20)
# # ---------------
#
# a = 10
# b = 0
# result = a / b
# print("Result:", result)
#
# print("#"*40, end="\n\n")
# #########################

print("Handling exceptions using try-except blocks")
print("-"*20)
# ---------------

try:
    a = 10
    b = 0
    result = a / b
    print("Result:", result)
except:
    print("Reached except block")
    print("Some error occurred in try-block")

# If any error in try block, program will NOT terminate
#       instead except-block will be executed
#       so, in except-block, we need to write code/logic
#       to take action for the error occured in try-block
# If NO error in try block, program will skip except-block

print("#"*40, end="\n\n")
#########################
# ---------------
# How it works?
# ---------------
# - If we want to handle exceptions using try-except blocks
#   then we need to have exception class for that error
#
# - If we don't have exception-class for any error then
#   we can't handle that error using try-except block.
#   program will terminate abruptly in the try-block itself.
#
# - Few exception classes are present in builtins
#
# - default except-block, knows all builtin exception classes
#   so, by default it can allow/accept/handle all builtin exceptions
#
# - Above block is throwing zero division error and class 'ZeroDivisionError'
#   is present in builtins. Thats why except-block will be able to handle.
#
# - While using libraries, libraries also provide exception classes
#   which we can use to handle errors coming while using that library.
#
# - If no class present then we need to write own exception class
#
# - 'Exception' class is super class for all exception classes
#########################

print("Complete list of builtins ")
print("-"*20)
# ---------------

print(dir(__builtins__))
# https://docs.python.org/3/library/index.html

print("#"*40, end="\n\n")
#########################
print("try-except blocks with class names")
print("-"*20)
# ---------------

try:
    L = ["Java", "Python"]
    print("100th Value:", L[100]) # Index Error
    a = 10
    b = 0
    result = a / b
    print("Result:", result)
except ZeroDivisionError: # 1-way: This is 1-way to specify class name
    print("This is ZDE")
except NameError as ne: # 2-way: Here capturing error message
    print("This is NameError and value of ne is:", ne)
except Exception as e:
    print("This is default except block and error message:", e)

print("#"*40, end="\n\n")
#########################
