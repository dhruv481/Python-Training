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