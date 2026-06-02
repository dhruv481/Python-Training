"""
Frozenset:
        - There is already a option to store MULTIPLE values like list of employee names
        - We can store UNIQUE values
        - No, Index number to each value
        - It is unordered and order of the values will be keep changing.
"""
print("Frozenset PART-1")
print("Store MULTIPLE UNQUE values")
print("-"*20)
# ---------------

#- We don't have any shortcut for frozenset. So,
# we need to use class name to create object

my_fs = frozenset(["emp-1", "emp-2", "emp-1", "emp-2", "emp-3"])
print(my_fs)

# If we want index number then we can convert to other types like
# list/tuple etc

print("#"*40, end="\n\n")
#########################
print("Frozenset PART-2")
print("METHODS present in frozenset class")
print("-"*20)
# ---------------

print(dir(my_fs), end="\n\n")
# OR
print(dir(frozenset))

print("#"*40, end="\n\n")
#########################

print("Frozenset PART-3")
print("union, intersection, difference methods")
print("-"*20)
# ---------------

enrolled_for_java_course = frozenset(["emp-1", "emp-2", "emp-3", "emp-4"])
print("enrolled_for_java_course", enrolled_for_java_course)

enrolled_for_python_course = frozenset(["emp-3", "emp-4", "emp-5", "emp-6" ])
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
