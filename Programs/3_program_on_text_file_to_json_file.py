"""
Get data from sample_data.log

then

extract
IP
DATE
URL

then

make dictionary with extracted data

then

write to my_report_2.json

Expected dictionary
my_dictionary = {
0 : ('123.123.123.123', ''26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
1 : ('123.123.123.123', ''26/Apr/2000', 'http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF'),
2 : ('123.123.123.123', ''26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
3 : ('123.123.123.123', ''26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
4 : ('123.123.123.123', ''26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
5 : ('123.123.123.123', ''26/Apr/2000', 'http://www.jafsoft.com/asctortf/')
}
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

# ---------------
# >>> # Our Plan
# ---------------
# >>> my_dictionary={}
# >>> # 1st Iteration
# >>> each_line_tuple = ('ip', 'dt', 'url')
# >>> my_dictionary[0] = each_line_tuple
# >>> my_dictionary
# {0: ('ip', 'dt', 'url')}
# >>> # 2nd Iteration
# >>> each_line_tuple = ('ip', 'dt', 'url')
# >>> my_dictionary[1] = each_line_tuple
# >>> my_dictionary
# {0: ('ip', 'dt', 'url'), 1: ('ip', 'dt', 'url')}
#########################

print("Extract IP, DATE, URL and make dictionary with extracted data")
print("-"*20)
# ---------------
my_dictionary = {}
key = 0
for line in log_file_content:
    if line.startswith("123"):
        sp = line.split()
        ip = sp[0]

        raw_date = sp[3] # '[26/Apr/2000:00:23:51'
        start_index = 1
        end_index = raw_date.find(":")
        dt = raw_date[start_index:end_index]

        raw_url = sp[10]
        url = raw_url.strip('"')
        each_line_tuple = (ip, dt, url)
        my_dictionary[key] = each_line_tuple
        key += 1

print("my_dictionary:", my_dictionary, end="\n\n")

print("#"*40, end="\n\n")
#########################
print("Write to my_report_2.json")
print("-"*20)
# ---------------

my_json_file_handle = open(file=r"my_report_2.json", mode="w")

import json
json.dump(my_dictionary, my_json_file_handle)# dump() is write() method

my_json_file_handle.close()

print("Created my_report_2.json, Please check")

print("#"*40, end="\n\n")
#########################