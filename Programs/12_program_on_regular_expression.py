"""
Get data from sample_data.log

then
IP
DATE
URL
using regular expression
"""

print("Dynamically making file path and reading from sample_data.log")
print("-"*20)
# ---------------

# __file__ : This is builtin variable, which is available in every program
print("__file__:", __file__, end="\n\n")

# Using __file__ may not work in all shell/terminal/like IDLE window

# os library
import os

abs_path = os.path.abspath(__file__) # This will work in any platform/any-shell
print("abs_path:", abs_path, end="\n\n")

parent_directory = os.path.dirname(abs_path)
print("parent_directory:", parent_directory, end="\n\n")

# 1-way: making full path
log_file_path = parent_directory +r"\sample_data.log"
print("log_file_path:", log_file_path, end="\n\n")

# 2-way: making full path
log_file_path = os.path.join(parent_directory, "sample_data.log")
print("log_file_path:", log_file_path, end="\n\n")

my_log_file_handle = open(file=log_file_path, mode="r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
#########################

print("Check whether line is starting with IP address or not?")
print("-"*20)
# ---------------
import re
for each_line in log_file_content:
    match_result = re.match(r'\d{3}\.\d{3}\.\d{3}\.\d{3}', each_line)
    print("Each Line:", each_line)
    print("match_result:", match_result)
    print("-"*10, end="\n\n")

# COMMENT - 2
r"""
In regular expression,

Identifiers
-----------------
\d -> use \d to tell any one digit
\D -> use \D to tell any one character except digits
. -> use . to tell any one any character
\. -> use \. to tell strictly DOT, not any character
\s -> to tell one space
\S -> to tell any one character except space
\w -> to tell any one character in this group [a-zA-Z0-9_]
\W -> to tell any one character except characters present in this group [a-zA-Z0-9_]
-----------------

Quantifiers
-----------------
\d{3} -> Exactly 3 digits
\d{1,3} -> It can be one digit or two digits or three digits
-----------------

Modifiers:
-----------------
* -> Use this to tell 0 or more times
+ -> Use this to tell 1 or more times
? -> Use this to tell 0 or one time
-----------------
"""

# COMMENT - 1
r"""
match_result = re.match(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d', each_line)
# OR
match_result = re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', each_line)
# OR
match_result = re.match(r'(\d{3}\.){3}\d{3}}', each_line)
"""


print("#"*40, end="\n\n")
#########################
print("Extract IP: ")
print("-"*20)
# ---------------
import re
for each_line in log_file_content:
    match_result = re.match(r'(\d{3}\.\d{3}\.\d{3}\.\d{3})', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        print("ip:", ip)

# COMMENT
r"""
put () to IP address pattern to capture IP
This is called grouping
Each group will be having index number starting from 1
"""

print("#"*40, end="\n\n")
#########################
print("Extract IP, DATE: ")
print("-"*20)
# ---------------
import re
for each_line in log_file_content:
    match_result = re.match(r'(\d{3}\.\d{3}\.\d{3}\.\d{3}).*(\d{2}/[a-zA-Z]{3}/\d{4})', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip, dt)

# COMMENT
r"""

Pattern for Date: 26/Apr/2000

26
--
\d\d # Exactly 2 digits
\d{2} # Exactly 2 digits
[0-9][0-9] # Exactly 2 digits
[0-9]{2} # Exactly 2 digits
[0-9]\d # Exactly 2 digits
\d[0-9] # Exactly 2 digits

\d{1,2} # minimum one, maximum two
[0-9]{1,2} # minimum one, maximum two
\d?\d # minimum one, maximum two
[0-9]?[0-9] # minimum one, maximum two
\d?[0-9] # minimum one, maximum two
[0-9]?\d # minimum one, maximum two
--

Apr
---
[A-Z][a-z][a-z]
# OR
[A-Z][a-z]{2}
# OR
[a-zA-Z]{3}
# OR
(Jan|Feb|Mar|Apr|May|Jun)
---
"""

print("#"*40, end="\n\n")
#########################
print("Extract IP, DATE, URL: ")
print("-"*20)
# ---------------
import re
for each_line in log_file_content:
    match_result = re.match(r'(\d{3}\.\d{3}\.\d{3}\.\d{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(http[s]?://[a-z./A-Z_]+)', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        url = match_result.group(3)
        print(ip, dt, url)

# COMMENT
r"""
http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

http[s]?://[a-z./A-Z_]+

http[s]? -> s is optional
https? -> s is optional
(https)? -> exact word https  is optional
[https] -> [] represent individual character. Any one character in this group of character

"""

print("#"*40, end="\n\n")
#########################
