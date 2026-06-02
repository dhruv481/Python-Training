"""
Get data from sample_data.log

then
IP
DATE
URL

then
write extracted data to my_report_1.txt

Expected content in my_report_1.txt
        IP                      DATE                            URL
123.123.123.123     26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000         http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123     26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000         http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000         http://www.jafsoft.com/asctortf/

"""
#print("Get data from sample_data.log")
#print("-"*20)
# ---------------

#my_log_file_handle = open(file=r"sample_data.log", mode="r")
#log_file_content = my_log_file_handle.readlines()
#my_log_file_handle.close()

#print(log_file_content)

#print("#"*40, end="\n\n")
#########################

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
print("Iterate using for loop")
print("-"*20)
# ---------------

for line in log_file_content:
    print("Each Line:", line)

print("#"*40, end="\n\n")
#########################

print("type of each line")
print("-"*20)
# ---------------

for line in log_file_content:
    print("Each Line:", type(line))

print("#"*40, end="\n\n")
#########################

print("Filter only IP address lines and print")
print("-"*20)
# ---------------

for line in log_file_content:
    if line.startswith("123"):
        print("Each Line:", line)

print("#"*40, end="\n\n")
#########################
print("Extract IP")
print("-"*20)
# ---------------

for line in log_file_content:
    if line.startswith("123"):
        sp = line.split()
        print("sp:", sp, end="\n\n")
        ip = sp[0]
        print("ip:", ip, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Extract IP, DATE")
print("-"*20)
# ---------------

for line in log_file_content:
    if line.startswith("123"):
        sp = line.split()
        print("sp:", sp, end="\n\n")

        ip = sp[0]
        print("ip:", ip, end="\n\n")

        raw_date = sp[3] # '[26/Apr/2000:00:23:51'
        start_index = 1
        end_index = raw_date.find(":")
        dt = raw_date[start_index:end_index]
        print("dt:", dt, end="\n\n")

print("#"*40, end="\n\n")
#########################
print("Extract IP, DATE, URL")
print("-"*20)
# ---------------

for line in log_file_content:
    if line.startswith("123"):
        print("Each Line:", line)
        sp = line.split()
        print("sp:", sp, end="\n\n")

        ip = sp[0]
        print("ip:", ip, end="\n\n")

        raw_date = sp[3] # '[26/Apr/2000:00:23:51'
        start_index = 1
        end_index = raw_date.find(":")
        dt = raw_date[start_index:end_index]
        print("dt:", dt, end="\n\n")

        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        # 1-way: Remove " from both sides
        url_1 = raw_url.strip('"') # Remove from both ends
        # 2-way: Remove " from both sides
        url_2 = raw_url.removeprefix('"').removesuffix('"') # double quote inside single quote
        # 2-way: Remove " from both sides
        raw_url_sp = raw_url.split('"') # double quote inside single quote
        print("raw_url_sp:", raw_url_sp, end="\n\n")
        url_3 = raw_url_sp[1]
        print(url_1, url_2, url_3, sep="\n", end="\n\n")
        print("-"*20, end="\n\n")

print("#"*40, end="\n\n")
#########################
print("Extract IP, DATE, URL and write to my_report_1.txt")
print("-"*20)
# ---------------

my_out_file_handle = open(file="my_report_1.txt", mode="w")

# Write heading
print("IP", "DATE", "URL", sep="\t", file=my_out_file_handle)

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
        print(ip, dt, url, sep="\t", file=my_out_file_handle)

my_out_file_handle.close()

print("Created my_report_1.txt file. Please check")

print("#"*40, end="\n\n")
#########################