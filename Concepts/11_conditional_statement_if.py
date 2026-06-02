"""
Conditional statement 'if': We can execute block of code based on the condition
"""
print("Using only 'if-blocks'")
print("-"*20)
# ---------------

x = 10
if (x == 10) and (x < 100):
    print("line-1: x is equal to 10")
    print("line-2: x is equal to 10")
    print("line-3: x is equal to 10")

if x > 10:
    print("line-1: x is greater than 10")
    print("line-2: x is greater than 10")
    print("line-3: x is greater than 10")

if x < 10:
    print("line-1: x is less than 10")
    print("line-2: x is less than 10")
    print("line-3: x is less than 10")

print("#"*40, end="\n\n")
#########################

print("Using 'if and elif blocks'")
print("-"*20)
# ---------------

x = 10
if (x == 10) and (x < 100):
    print("line-1: x is equal to 10")
    print("line-2: x is equal to 10")
    print("line-3: x is equal to 10")

elif x > 10:
    print("line-1: x is greater than 10")
    print("line-2: x is greater than 10")
    print("line-3: x is greater than 10")

elif x < 10:
    print("line-1: x is less than 10")
    print("line-2: x is less than 10")
    print("line-3: x is less than 10")

print("#"*40, end="\n\n")
#########################

print("Using 'if, elif and else blocks'")
print("-" * 20)
# ---------------

x = 10
if (x == 10) and (x < 100):
    print("line-1: x is equal to 10")
    print("line-2: x is equal to 10")
    print("line-3: x is equal to 10")

elif x > 10:
    print("line-1: x is greater than 10")
    print("line-2: x is greater than 10")
    print("line-3: x is greater than 10")

else:
    print("line-1: x is less than 10")
    print("line-2: x is less than 10")
    print("line-3: x is less than 10")

print("#" * 40, end="\n\n")
#########################
print("Using if with collection classes to verify whether some values are present or not")
print("-"*20)
# ---------------

my_string = "Python"
print("my_string: ", my_string, end="\n\n")

if 'th' in my_string:
    print("sub string found")


my_list = ["emp-1", "emp-2", "emp-3", "emp-4"]
print("my_list: ", my_list, end="\n\n")

if "emp-3" in my_list:
    print("'emp-3 found'")

print("#"*40, end="\n\n")
#########################