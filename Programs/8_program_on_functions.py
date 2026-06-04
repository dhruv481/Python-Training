"""
Assume we are regularly getting log files.
from each file,
- we need to read log file
- we need to extract info
- we need to write to either text file or json file

Here we are planning for 3 functions:
Function-1: log_process_function
This function will take only one argument log_file_path
then  This function will read log file then
This function will extract information
then This function will return extracted data in list of tuples

Function-2: write_to_text_file_function
This function will take 2 arguments
1) extracted data and 2) output_file_path
then This function will write extracted data output_file_path

Function-3: write_to_json_file_function
This function will take 2 arguments
1) extracted data and 2) output_file_path
then This function will write extracted data output_file_path
"""
"""
Python coding style guide
https://peps.python.org/pep-0008/
"""

print("Function-1: Extract_Info_Function")
print("-"*20)
# ---------------

def extract_info_function(log_file_path):
    """
    This function will take only one argument log_file_path
    then  This function will read log file then
    This function will extract information
    then This function will return extracted data in list of tuples
    :param log_file_path:
    :return extracted_data:
    """
    # ---------------
    # Get data from log file
    # ---------------
    import os
    abs_path = os.path.abspath(__file__)
    parent_directory = os.path.dirname(abs_path)
    log_file_path = os.path.join(parent_directory, log_file_path)

    my_log_file_handle = open(file=log_file_path, mode="r")
    log_file_content = my_log_file_handle.readlines()
    my_log_file_handle.close()
    #########################

    # ---------------
    # Extract info and return in list of tuples
    # ---------------
    my_list = []
    for line in log_file_content:
        if line.startswith("123"):
            sp = line.split()
            ip = sp[0]

            raw_date = sp[3]  # '[26/Apr/2000:00:23:51'
            start_index = 1
            end_index = raw_date.find(":")
            dt = raw_date[start_index:end_index]

            raw_url = sp[10]
            url = raw_url.strip('"')

            each_line_tuple = (ip, dt, url)
            my_list.append(each_line_tuple)
    return my_list
    #########################

print("#"*40, end="\n\n")
#########################

print("Testing Function-1: Extract_Info_Function")
print("-"*20)
# ---------------

received_data = extract_info_function("sample_data.log")
print(received_data)

print("#"*40, end="\n\n")
#########################
print("Function-2: write_to_text_file_function")
print("-"*20)
# ---------------

def write_to_text_file_function(extracted_data, output_file_path):
    """
    This function will take 2 arguments
    1) extracted data and 2) output_file_path
    then This function will write extracted data output_file_path
    :param extracted_data:
    :param output_file_path:
    :return None:
    """
    # Extracted Data: [('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/')]
    my_out_file_handle = open(file=output_file_path, mode="w")
    print("IP", "DATE", "URL", sep="\t", file=my_out_file_handle)
    for each_line_tuple in extracted_data:
        ip = each_line_tuple[0]
        dt = each_line_tuple[1]
        url = each_line_tuple[2]
        print(ip, dt, url, sep="\t", file=my_out_file_handle)
    my_out_file_handle.close()

print("#"*40, end="\n\n")
#########################

print("Testing Function-2: write_to_text_file_function")
print("-"*20)
# ---------------

write_to_text_file_function(received_data, "my_report_5.txt")
print("Created 'my_report_5.txt'. Please check")

print("#"*40, end="\n\n")
#########################
print("Function-2: write_to_text_file_function")
print("-"*20)
# ---------------

def write_to_text_file_function(extracted_data, output_file_path):
    """
    This function will take 2 arguments
    1) extracted data and 2) output_file_path
    then This function will write extracted data output_file_path
    :param extracted_data:
    :param output_file_path:
    :return None:
    """
    # Extracted Data: [('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/')]
    my_out_file_handle = open(file=output_file_path, mode="w")
    print("IP", "DATE", "URL", sep="\t", file=my_out_file_handle)
    for each_line_tuple in extracted_data:
        ip = each_line_tuple[0]
        dt = each_line_tuple[1]
        url = each_line_tuple[2]
        print(ip, dt, url, sep="\t", file=my_out_file_handle)
    my_out_file_handle.close()

print("#"*40, end="\n\n")
#########################

print("Testing Function-2: write_to_text_file_function")
print("-"*20)
# ---------------

write_to_text_file_function(received_data, "my_report_5.txt")
print("Created 'my_report_5.txt'. Please check")

print("#"*40, end="\n\n")
#########################
print("Function-3: write_to_json_file_function")
print("-"*20)
# ---------------

def write_to_json_file_function(extracted_data, output_file_path):
    """
    This function will take 2 arguments
    1) extracted data and 2) output_file_path
    then This function will write extracted data output_file_path
    :param extracted_data:
    :param output_file_path:
    :return None:
    """
    # Extracted Data: [('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),('123.123.123.123', '26/Apr/2000', 'http://www.jafsoft.com/asctortf/')]
    my_out_file_handle = open(file=output_file_path, mode="w")
    import json
    json.dump(extracted_data, my_out_file_handle)
    my_out_file_handle.close()

print("#"*40, end="\n\n")
#########################

print("Testing Function-3: write_to_json_file_function")
print("-"*20)
# ---------------

write_to_json_file_function(received_data, "my_report_6.json")
print("Created 'my_report_6.json'. Please check")

print("#"*40, end="\n\n")
#########################
