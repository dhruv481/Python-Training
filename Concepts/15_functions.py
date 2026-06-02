"""
Functions: If we want to rewrite/copy-paste same code more
than one time in our program then instead of rewrite/copy-paste same code more
than one time in our program, we can keep that code in a block and reuse.
"""
print("WITHOUT using function")
print("-"*20)
# ---------------

a = 10
b = 20
c = a + b
print("Value of c:", c, end="\n\n")

a = 10
b = 20
c = a + b
print("Value of c:", c, end="\n\n")

a = 10
b = 20
c = a + b
print("Value of c:", c, end="\n\n")

a = 10
b = 20
c = a + b
print("Value of c:", c, end="\n\n")

a = 10
b = 20
c = a + b
print("Value of c:", c, end="\n\n")

a = 10
b = 20
c = a + b
print("Value of c:", c, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("USING function")
print("-"*20)
# ---------------

# Function Definition
def my_function():
    a = 10
    b = 20
    c = a + b
    print("Value of c:", c, end="\n\n")

# Function Call
my_function()
my_function()
my_function()
my_function()
my_function()

print("#"*40, end="\n\n")
#########################