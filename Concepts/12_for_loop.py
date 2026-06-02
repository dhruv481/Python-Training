"""
for-loop: Use this to iterate any collection like string, list, tuple etc.
"""
print("Iterate strings")
print("-"*20)
# ---------------

my_string = "Python"
print("my_string: ", my_string, end="\n\n")

for i in my_string:
    print("line-1: processing value:", i)
    print("line-2: processing value:", i)
    print("line-3: processing value:", i, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Iterate list")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-4"]
print("my_list: ", my_list, end="\n\n")

for i in my_list:
    print("line-1: processing value:", i)
    print("line-2: processing value:", i)
    print("line-3: processing value:", i, end="\n\n")

print("#"*40, end="\n\n")
#########################
print("'break-statement:' MANUALLY We can end for-loop whenever we need it. ")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-4", "emp-5"]
print("my_list: ", my_list, end="\n\n")

# End for-loop if the value is equal to 'emp-3'

for i in my_list:
    print("line-1: processing value:", i)
    print("line-2: processing value:", i)
    print("line-3: processing value:", i, end="\n\n")
    if i == "emp-3":
        print("Got Value 'emp-3'")
        print("MANUALLY ending for-loop using 'break-statement''")
        break

print("#"*40, end="\n\n")
#########################
print("continue-statement:' MANUALLY We can skip iteration whenever we need it. ")
print("-"*20)
# ---------------

my_list = ["emp-1",  "emp-3","emp-2", "emp-3", "emp-4",  "emp-3", "emp-5"]
print("my_list: ", my_list, end="\n\n")

#  if the value is equal to 'emp-3' then skip the current iteration
# and go for next iteration. Because that value is not required
# to process.

for i in my_list:
    if i == "emp-3":
        print("Got Value 'emp-3'")
        print("MANUALLY sending it for next iteration using 'continue-statement''", end="\n\n")
        continue
    print("line-1: processing value:", i)
    print("line-2: processing value:", i)
    print("line-3: processing value:", i, end="\n\n")

print("#"*40, end="\n\n")
#########################
print("'for-else' block: We have 'else' block with for-loop")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-4", "emp-5"]
print("my_list: ", my_list, end="\n\n")

for i in my_list:
    print("Processing value:", i)
else:
    print("Reached for-else block")
    print("All the values are processed.")
    print("After completing for-loop, This else block will execute.")
    print("""In this block, we are writing logic to
    close-file connection,
    close DB,
     or some cleanup to do after completing for-loop""", end="\n\n")

# How it will work?
# after completing the for-loop, else block will execute.

print("#"*40, end="\n\n")
#########################
