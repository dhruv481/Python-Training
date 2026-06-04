"""
For log process activity, we need to provide 3 functionalities,
that is,
1. extract_info
2. write_to_txt
3. write_to_json

Since, for one task/requirement, we need to provide more than
one functions then instead of writing 3 functions, we can
write one class and 3 methods.

In this program, we are writing class for log process activity.

Expected Class:
l1 = LogProcessClass("sample_data.txt")
received_data = l1.extract_info()
# received_data = [(ip, dt, url),(),()]
l1.write_to_txt("sample_data.txt")
l1.write_to_json("sample_data.json")
"""
print("Writing 'LogProcessClass':")
print("-"*20)
# ---------------

class LogProcessClass:
    def __init__(self, log_file_path):
        # 1-way: We are keeping only file path
        self.log_file_path = log_file_path
        # 2-way: read file content and keep it
        import os
        abs_path = os.path.abspath(__file__)
        parent_directory = os.path.dirname(abs_path)
        log_file_path = os.path.join(parent_directory, log_file_path)
        my_log_file_handle = open(file=log_file_path, mode="r")
        self.log_file_content = my_log_file_handle.readlines()
        my_log_file_handle.close()

    def extract_info(self):
        my_list = []
        for line in self.log_file_content:
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
    def write_to_txt(self, output_file_path):
        # Get data
        extracted_data = self.extract_info()
        # Write to file
        my_out_file_handle = open(file=output_file_path, mode="w")
        print("IP", "DATE", "URL", sep="\t", file=my_out_file_handle)
        for each_line_tuple in extracted_data:
            ip = each_line_tuple[0]
            dt = each_line_tuple[1]
            url = each_line_tuple[2]
            print(ip, dt, url, sep="\t", file=my_out_file_handle)
        my_out_file_handle.close()
    def write_to_json(self, output_file_path):
        # Get extracted data
        extracted_data = self.extract_info()
        # Write to json file
        my_out_file_handle = open(file=output_file_path, mode="w")
        import json
        json.dump(extracted_data, my_out_file_handle)
        my_out_file_handle.close()

print("#"*40, end="\n\n")
#########################

print("Testing 'LogProcessClass':")
print("-"*20)
# ---------------

l1 = LogProcessClass("sample_data.log")
received_data = l1.extract_info()
print("received_data:", received_data, end="\n\n")

l1.write_to_txt("my_report_7.txt")
l1.write_to_json("my_report_8.json")

print("Created my_report_7.txt and my_report_8.json")

print("#"*40, end="\n\n")
#########################