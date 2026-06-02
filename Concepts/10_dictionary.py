"""
Dictionary:
        - There is already a option to store MULTIPLE values like list of employee names
        - We can store DUPLICATE values
        - MANUALLY, we need to provide index to each value. Called KEY/VALUE pair
"""
print("Dictionary PART-1")
print("-"*20)
# ---------------

my_dictionary_1 = {0:5, 1:"python", 2:"online"}
print("my_dictionary_1:", my_dictionary_1, end="\n\n")

# For Keys: We can use int, string, tuple
# For Values: We can store any type of values inside dictionary

my_dictionary_2 = {
    "duration" : 5,
    "course" : "python",
    "mode": ["online", "classroom"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary_2:", my_dictionary_2, end="\n\n")

print("#"*40, end="\n\n")
#########################
print("Dictionary PART-2")
print("Accessing individual values")
print("-"*20)
# ---------------

my_dictionary = {
    "duration" : 5,
    "course" : "python",
    "mode": ["online", "classroom"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n")

print("Course:", my_dictionary["course"]) # "python"
print("3rd character in Course:", my_dictionary["course"][2], end="\n\n") # "t"

print("Mode:", my_dictionary["mode"]) # ["online", "classroom"]
print("1st Mode:", my_dictionary["mode"][0]) # "online"
print("3rd character in 1st Mode:", my_dictionary["mode"][0][2], end="\n\n") # "l"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("fname of the Trainer:", my_dictionary["trainer"]["fname"]) # "abc"
print("2nd character in fname of the Trainer:", my_dictionary["trainer"]["fname"][1], end="\n\n") # "b"

print("#"*40, end="\n\n")
#########################
print("Dictionary PART-3")
print("METHODS present in 'dict' class")
print("-"*20)
# ---------------

print(dir(my_dictionary), end="\n\n")
# OR
print(dir(dict))

print("#"*40, end="\n\n")
#########################

print("Dictionary PART-4")
print("Add/Remove/Update")
print("-"*20)
# ---------------

my_dictionary = {
    "duration" : 5,
    "course" : "python"
}
print("my_dictionary:", my_dictionary, end="\n\n")

# Add/Update: Same procedure
my_dictionary["course"] = "Java" # Key present so it will UPDATE
my_dictionary["location"] = "XYZ Location" # Key not present So, it will add
print("my_dictionary after adding location and updating course:", my_dictionary, end="\n\n")

# Remove duration
my_dictionary.pop("duration")
print("my_dictionary after removing duration:", my_dictionary, end="\n\n")

print("#"*40, end="\n\n")
#########################
