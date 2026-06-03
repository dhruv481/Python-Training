"""
How to add methods?
"""
"""
Requirement:
1. Write method to store company details inside CLASS OBJECT
2. Write method to get company details from CLASS OBJECT
3. Write method to store employee details inside INSTANCE OBJECT
4. Write method to get employee details from INSTANCE OBJECT
5. Write method to convert to uppercase
6. Write method to convert to lowercase
7. write method to get company details from CLASS OBJECT and
    store it in json file
8. write method to get company details from json file
"""

"""
Which object access we need inside each method

1. Write method to store company details inside CLASS OBJECT
    - Inside this method, we need access to CLASS OBJECT

2. Write method to get company details from CLASS OBJECT
    - Inside this method, we need access to CLASS OBJECT

3. Write method to store employee details inside INSTANCE OBJECT
    - Inside this method, we need access to INSTANCE OBJECT

4. Write method to get employee details from INSTANCE OBJECT
    - Inside this method, we need access to INSTANCE OBJECT

5. Write method to convert to uppercase
    - Inside this method, we need access to INSTANCE OBJECT

6. Write method to convert to lowercase
    - Inside this method, we need access to INSTANCE OBJECT

7. write method to get company details from CLASS OBJECT and
    store it in json file
    - Inside this method, we need access to CLASS OBJECT

8. write method to get company details from json file
    - We DON'T need access to any of the object
        -- We DON'T need access to INSTANCE object
        -- We DON'T need access to CLASS object
"""
"""
In this program, we are implementing below 2 methods

1. Write method to store company details inside CLASS OBJECT
    - Inside this method, we need access to CLASS OBJECT

2. Write method to get company details from CLASS OBJECT
    - Inside this method, we need access to CLASS OBJECT
"""

print("Writing Employee Class")
print("-"*20)
# ---------------

class Employee:
    # 1. Write method to store company details inside CLASS OBJECT
    #     - Inside this method, we need access to CLASS OBJECT
    @classmethod # It will take care of passing class object to cls
    def store_company_details(cls, company_name, company_location):
        cls.company_name = company_name
        cls.company_location = company_location

    # 2. Write method to get company details from CLASS OBJECT
    #     - Inside this method, we need access to CLASS OBJECT
    @classmethod
    def get_company_details(cls):
        company_details = {"company_name": cls.company_name, "company_location": cls.company_location}
        return company_details

print("#"*40, end="\n\n")
#########################

print("Testing Employee Class")
print("-"*20)
# ---------------

Employee.store_company_details("XYZ Company", "XYZ Location")
# Internally, object 'Employee' will get passed to 1st argument 'cls'

company_details = Employee.get_company_details()
# Internally, object 'Employee' will get passed to 1st argument 'cls'
print("company_details:", company_details, end="\n\n")

print("#"*40, end="\n\n")
#########################