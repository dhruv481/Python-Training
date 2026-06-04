"""
Assume we are regularly getting log files.
from each file,
- we need to read log file
- we need to extract info
- we need to write to text file

Since we want to repeat above steps for every file, we
are planning write function.

Expected Function:
function name: log_process_function
function argument: log_file_path, out_file_path
function should read log file, extract and write to text file

Example:
    log_process_function("sample_data.log", "my_report_10.txt")
"""
def log_process_function(log_file_path, out_file_path):
    """
    function should read log file, extract and write to text file
    :param log_file_path:
    :param out_file_path:
    :return None:
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
    # Extract info and write to output file
    # ---------------
    my_out_file_handle = open(file=out_file_path, mode="w")

    # Write heading
    print("IP", "DATE", "URL", sep="\t", file=my_out_file_handle)

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
            print(ip, dt, url, sep="\t", file=my_out_file_handle)
    my_out_file_handle.close()
    #########################
print("#"*40, end="\n\n")
#########################

print("Testing log_process_function")
print("-"*20)
# ---------------
log_process_function("sample_data.log", "my_report_4.txt")
print("Created my_report_4.txt, please check")
print("#"*40, end="\n\n")
#########################