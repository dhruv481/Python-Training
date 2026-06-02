"""
while-loop: We can provide the condition and, we run the loop till that condition is True.
"""

print("While loop example:")
print("-"*20)
# ---------------

x = 0
while x < 5:
    print("Line-1: Value of x is:", x)
    print("Line-2: Value of x is:", x)
    print("Line-3: Value of x is:", x, end="\n\n")
    x = x + 1

print("#"*40, end="\n\n")
#########################
print("'break-statement:' MANUALLY We can end while-loop whenever we need it. ")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-4", "emp-5"]
print("my_list: ", my_list, end="\n\n")

# End while-loop if the value is equal to 'emp-3'
index_no = 0
while index_no < len(my_list):
    i = my_list[index_no]
    index_no = index_no + 1
    print("line-1: processing value:", i)
    print("line-2: processing value:", i)
    print("line-3: processing value:", i, end="\n\n")
    if i == "emp-3":
        print("Got Value 'emp-3'")
        print("MANUALLY ending while-loop using 'break-statement''")
        break

# Using for-loop

# End for-loop if the value is equal to 'emp-3'
# for i in my_list:
#     print("line-1: processing value:", i)
#     print("line-2: processing value:", i)
#     print("line-3: processing value:", i, end="\n\n")
#     if i == "emp-3":
#         print("Got Value 'emp-3'")
#         print("MANUALLY ending for-loop using 'break-statement''")
#         break

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

index_no = 0
while index_no < len(my_list):
    i = my_list[index_no]
    index_no = index_no + 1
    if i == "emp-3":
        print("Got Value 'emp-3'")
        print("MANUALLY sending it for next iteration using 'continue-statement''", end="\n\n")
        continue
    print("line-1: processing value:", i)
    print("line-2: processing value:", i)
    print("line-3: processing value:", i, end="\n\n")

# Using for-loop

#  if the value is equal to 'emp-3' then skip the current iteration
# and go for next iteration. Because that value is not required
# to process.

# for i in my_list:
#     if i == "emp-3":
#         print("Got Value 'emp-3'")
#         print("MANUALLY sending it for next iteration using 'continue-statement''", end="\n\n")
#         continue
#     print("line-1: processing value:", i)
#     print("line-2: processing value:", i)
#     print("line-3: processing value:", i, end="\n\n")

print("#"*40, end="\n\n")
#########################
print("'while-else' block: We have 'else' block with while-loop")
print("-"*20)
# ---------------

my_list = ["emp-1", "emp-2", "emp-3", "emp-4", "emp-5"]
print("my_list: ", my_list, end="\n\n")

index_no = 0
while index_no < len(my_list):
    i = my_list[index_no]
    index_no = index_no + 1
    print("Processing value:", i)
else:
    print("Reached while-else block")
    print("All the values are processed.")
    print("After completing while-loop, This else block will execute.")
    print("""In this block, we are writing logic to
    close-file connection,
    close DB,
     or some cleanup to do after completing while-loop""", end="\n\n")

# How it will work?
# after completing the while-loop, else block will execute.

# Using for-loop

# for i in my_list:
#     print("Processing value:", i)
# else:
#     print("Reached for-else block")
#     print("All the values are processed.")
#     print("After completing for-loop, This else block will execute.")
#     print("""In this block, we are writing logic to
#     close-file connection,
#     close DB,
#      or some cleanup to do after completing for-loop""", end="\n\n")

# How it will work?
# after completing the for-loop, else block will execute.

print("#"*40, end="\n\n")
#########################
