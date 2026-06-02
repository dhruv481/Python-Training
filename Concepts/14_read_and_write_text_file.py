"""
Read and write to text file
- File which is having words, sentences, paragraphs, etc.
- File can be using any extension like .txt, .log etc
"""

"""
To read or write we need to follow 3 steps
Step-1: Connect to file
Step-2: Read and write to text file
Step-3: Disconnect from file
"""

"""
We have functions/methods for all 3 steps
Step-1: Connect to file
    - open() FUNCTION

Step-2: Read and write to text file
    - FOR WRITING:
        1) write() METHOD:
            - Use this to write SINGLE value
        2) writelines() METHOD:
            - Use this to write MULTIPLE values(list/tuple etc)
        3) print() FUNCTION
            - We can use this to write both SINGLE and MULTIPLE values

    - FOR READING:
        1) read() METHOD
            - Use this to get entire file content in one STRING
        2) readlines() METHOD
            - Use this to get entire file content in one LIST
        3) readline() METHOD
            - Use this to get one line

Step-3: Disconnect from file
    - close() METHOD
"""
# ---------------
# Different Modes
# ---------------
# mode "w":
#   - Write only mode
#   - This mode will create new file
#   - IMPORTANT: This mode will erase existing file content
#
# mode "r":
#   - Read only mode
#   - This mode will NOT create new file
#
# mode "a":
#   - Append/Write only mode
#   - This mode will create new file only if file not present
#   - This mode will append to existing file content
#
# NOTE:
#   - if we add + to any mode then it will enable both
#       read and write mode
#   - Example: 'w+', 'r+', 'a+'
#   - read & write mode means, using same file handle,
#       we can call both read methods and write methods.
#########################
print("All write operations")
print("-"*20)
# ---------------

# Step-1: Connect to file
# ---------------
# my_file_handle = open(file=r"provide file name or file path", mode="provide mode here")
my_file_handle = open(file=r"my_out_file.txt", mode="w")

# Step-2: Write to text file
# ---------------

# Our Data
x = 10
y = "Python"

#         1) write() METHOD:
#             - Use this to write SINGLE value
my_file_handle.write(str(x)+"\n") # we need to pass string
my_file_handle.write(y+"\n")

#         2) writelines() METHOD:
#             - Use this to write MULTIPLE values(list/tuple etc)
my_list = [str(x)+"\n", y+"\n"]
my_file_handle.writelines(my_list)

#         3) print() FUNCTION
#             - We can use this to write both SINGLE and MULTIPLE values
print(x, y, 20, "Java", sep="\n", file=my_file_handle)
# file=my_file_handle : print will write to file not to console
# x, 20 -> No need of converting to string

# Step-3: Disconnect from file
# ---------------
my_file_handle.close()

print("All write operations are done. Please check 'my_out_file.txt'")

print("#"*40, end="\n\n")
#########################