"""
set:
        - There is already an option to store MULTIPLE values like list of employee names
        - We can store UNIQUE values
        - No, Index number to each value
        - It is unordered and order of the values will be keep changing.
"""
print("set PART-1")
print("Store MULTIPLE UNQUE values")
print("-"*20)
# ---------------

my_set = {"emp-1", "emp-2", "emp-1", "emp-2", "emp-3"}
print(my_set)
# OR
my_set = set(["emp-1", "emp-2", "emp-1", "emp-2", "emp-3"])
print(my_set)

# If we want index number then we can convert to other types like
# list/tuple etc

print("#"*40, end="\n\n")
#########################

print("set PART-2")
print("METHODS present in set class")
print("-"*20)
# ---------------

print(dir(my_set), end="\n\n")
# OR
print(dir(set))

print("#"*40, end="\n\n")
#########################

print("set PART-3")
print("union, intersection, difference methods")
print("-"*20)
# ---------------

enrolled_for_java_course = {"emp-1", "emp-2", "emp-3", "emp-4"}
print("enrolled_for_java_course", enrolled_for_java_course)

enrolled_for_python_course = set(["emp-3", "emp-4", "emp-5", "emp-6" ])
print("enrolled_for_python_course", enrolled_for_python_course)

# Union
total_employees = enrolled_for_python_course.union(enrolled_for_java_course)
print("total_employees", total_employees)

# Intersection
registered_for_both = enrolled_for_java_course.intersection(enrolled_for_python_course)
print("registered_for_both", registered_for_both)

# Difference
only_java = enrolled_for_java_course.difference(enrolled_for_python_course)
print("only_java", only_java)

print("#"*40, end="\n\n")
#########################

print("set PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# ---------------

enrolled_for_java_course = {"emp-1", "emp-2", "emp-3", "emp-4"}
print("enrolled_for_java_course", enrolled_for_java_course)

enrolled_for_python_course = set(["emp-3", "emp-4", "emp-5", "emp-6" ])
print("enrolled_for_python_course", enrolled_for_python_course)

# Add
enrolled_for_python_course.add("emp-100")
print("enrolled_for_python_course after adding emp-100", enrolled_for_python_course)

# Remove 'emp-5'
enrolled_for_python_course.remove("emp-6")
print("enrolled_for_python_course after removing emp-6", enrolled_for_python_course)

# Update
enrolled_for_python_course.update(enrolled_for_java_course)
print("enrolled_for_python_course:", enrolled_for_python_course)

print("#"*40, end="\n\n")
#########################