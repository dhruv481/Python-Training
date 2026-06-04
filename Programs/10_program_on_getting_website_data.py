"""
Reading website data
Library: requests
Library Documentation: https://pypi.org/project/requests/
"""

print("Getting website data")
print("-"*20)
# ---------------

import requests
response = requests.get("http://www.python.org/")
web_content = response.text
print(web_content)

print("#"*40, end="\n\n")
#########################