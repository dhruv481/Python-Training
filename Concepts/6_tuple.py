"""
Tuple:
        - There is already a option to store MULTIPLE values like list of employee names
        - We can store DUPLICATE values
        - Automatically index number will be assigned to each value
"""
print("Tuple PART-1")
print("Store MULTIPLE values")
print("-"*20)
# ---------------

my_tuple = (10, 12.5, "Python", ("Online", "Offline"))
print(my_tuple)

print("#"*40, end="\n\n")
#########################

# ---------------
# Indexes
# ---------------
# Indexes are similar to strings. So all 4 options tried
# in strings will work here as well
#########################

print("Tuple PART-2")
print("Access each value")
print("-"*20)
# ---------------

my_tuple = (10, 12.5, "Python", ("Online", "Offline"))
print("my_tuple", my_tuple, end="\n\n")

print("0th Value:", my_tuple[0], end="\n\n")

print("1st Value:", my_tuple[1], end="\n\n")

print("2nd Value:", my_tuple[2]) # Python
print("3rd character in 2nd Value:", my_tuple[2][2], end="\n\n") # P

print("3rd Value:", my_tuple[3]) # ("Online", "Offline")
print("Last Mode in 3rd Value:", my_tuple[3][-1]) # "Offline"
print("3rd character in Last Mode in 3rd Value:", my_tuple[3][-1][2], end="\n\n") # "f"

print("#"*40, end="\n\n")
#########################
print("Tuple PART-3")
print("List of methods present inside tuple class")
print("-"*20)
# ---------------

print(dir(my_tuple), end="\n\n")
# OR
print(dir(tuple))

print("#"*40, end="\n\n")
#########################

print("Tuple PART-4")
print("count and index methods")
print("-"*20)
# ---------------

my_tuple = ("emp-1", "emp-2", "emp-1", "emp-3", "emp-4")
print("my_tuple", my_tuple, end="\n\n")

count_of_emp_1 = my_tuple.count("emp-1") # 2
index_of_emp_1 = my_tuple.index("emp-1") # 0, returns index of 1st occurrance of emp-1

print("count_of_emp_1:", count_of_emp_1)
print("index_of_emp_1:", index_of_emp_1)

print("#"*40, end="\n\n")
#########################
