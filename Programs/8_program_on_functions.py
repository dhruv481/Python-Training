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