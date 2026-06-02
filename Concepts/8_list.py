"""
list:
        - There is already an option to store MULTIPLE values like list of employee names
        - We can store DUPLICATE values
        - Automatically index number will be assigned to each value
"""
print("list PART-1")
print("Store MULTIPLE values")
print("-"*20)
# ---------------

my_list = [10, 12.5, "Python", ("Online", "Offline")]
print(my_list)

print("#"*40, end="\n\n")
#########################

# ---------------
# Indexes
# ---------------
# Indexes are similar to strings. So all 4 options tried
# in strings will work here as well
#########################

print("list PART-2")
print("Access each value")
print("-"*20)
# ---------------

my_list = [10, 12.5, "Python", ("Online", "Offline")]
print("my_list", my_list, end="\n\n")

print("0th Value:", my_list[0], end="\n\n")

print("1st Value:", my_list[1], end="\n\n")

print("2nd Value:", my_list[2]) # Python
print("3rd character in 2nd Value:", my_list[2][2], end="\n\n") # P

print("3rd Value:", my_list[3]) # ("Online", "Offline")
print("Last Mode in 3rd Value:", my_list[3][-1]) # "Offline"
print("3rd character in Last Mode in 3rd Value:", my_list[3][-1][2], end="\n\n") # "f"

print("#"*40, end="\n\n")
#########################

print("list PART-3")
print("List of methods present inside list class")
print("-"*20)
# ---------------

print(dir(my_list), end="\n\n")
# OR
print(dir(list))

print("#"*40, end="\n\n")
#########################

print("list PART-4")
print("count and index methods")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-1", "emp-3", "emp-4"]
print("my_list", my_list, end="\n\n")

count_of_emp_1 = my_list.count("emp-1") # 2
index_of_emp_1 = my_list.index("emp-1") # 0, returns index of 1st occurrance of emp-1

print("count_of_emp_1:", count_of_emp_1)
print("index_of_emp_1:", index_of_emp_1)

print("#"*40, end="\n\n")
#########################
print("list PART-5")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2"]
print("my_list", my_list, end="\n\n")

# Add
my_list.append("emp-3")
print("my_list after adding new value emp-3:", my_list, end="\n\n")

# Update
my_list[1] = "emp-200"
print("my_list after updating 2nd value with emp-200", my_list, end="\n\n")

# Remove emp-1 at index-0
my_list.pop(0)
print("my_list after removing emp-0:", my_list, end="\n\n")


print("#"*40, end="\n\n")
#########################
