"""
2 cases:
Case-1: How to access values outside the function?
Case-2: How to pass values to variables present inside the function?

In this program, we will discuss
Case-1: How to access values outside the function?
"""
# ---------------
# 2 steps
# ---------------
# Step-1: Inside function, use 'return' statement to specify values to send outside
# Step-2: outside function, while calling function, assign function call to
#               to some variable so that return value from the function will be stored
#########################

print("Function with returning SINGLE value")
print("-"*20)
# ---------------

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Employee Name:", name)
    print("Company Name:", company, end="\n\n")
    # Step-1: Inside function, use 'return' statement to specify values to send outside
    return name

# Step-2: outside function, while calling function, assign function call to
#               some variable so that return value from the function will be stored
received_value = employee()
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Function with returning MULTIPLE values: TUPLE")
print("-"*20)
# ---------------

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Employee Name:", name)
    print("Company Name:", company, end="\n\n")
    # Step-1: Inside function, use 'return' statement to specify values to send outside
    return (name, company)

# Step-2: outside function, while calling function, assign function call to
#               some variable so that return value from the function will be stored
received_value = employee()
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Function with returning MULTIPLE values: LIST")
print("-"*20)
# ---------------

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Employee Name:", name)
    print("Company Name:", company, end="\n\n")
    # Step-1: Inside function, use 'return' statement to specify values to send outside
    return [name, company]

# Step-2: outside function, while calling function, assign function call to
#               some variable so that return value from the function will be stored
received_value = employee()
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Function with returning MULTIPLE values: DICTIONARY")
print("-"*20)
# ---------------

def employee():
    name = "emp-1"
    company = "comp-1"
    print("Employee Name:", name)
    print("Company Name:", company, end="\n\n")
    # Step-1: Inside function, use 'return' statement to specify values to send outside
    return {"name": name, "company": company}

# Step-2: outside function, while calling function, assign function call to
#               some variable so that return value from the function will be stored
received_value = employee()
print("received_value:", received_value, end="\n\n")

print("#"*40, end="\n\n")
#########################
