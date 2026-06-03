"""
Inheritance:
1. multilevel inheritance
2. multiple inheritance

In this program, we are,
1. multilevel inheritance
"""

print("Release-1:")
print("-"*20)
# ---------------
class EmployeeClassRelease1:
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

print("Release-2:")
print("-"*20)
# ---------------
# Inheritance
# EmployeeClassRelease2 is extending from EmployeeClassRelease1
# Whatever there in EmployeeClassRelease1 will come to EmployeeClassRelease2
class EmployeeClassRelease2(EmployeeClassRelease1):
    # 3. Write method to store employee details inside INSTANCE OBJECT
    #     - Inside this method, we need access to INSTANCE OBJECT

    # by default, any method will take instance object as 1st argument
    def store_employee_details(self, name, email, phone=None):
        self.name = name
        self.email = email
        self.phone = phone

    # 4. Write method to get employee details from INSTANCE OBJECT
    #     - Inside this method, we need access to INSTANCE OBJECT
    def get_employee_details(self):
        employee_details = {"name": self.name, "email": self.email, "phone": self.phone}
        return employee_details

print("#"*40, end="\n\n")
#########################

print("Release-3:")
print("-"*20)
# ---------------
# Inheritance
# EmployeeClassRelease3 is extending from EmployeeClassRelease2
# Whatever there in EmployeeClassRelease2 will come to EmployeeClassRelease3
class EmployeeClassRelease3(EmployeeClassRelease2):
    # 5. Write method to convert to uppercase
    #     - Inside this method, we need access to INSTANCE OBJECT
    def to_uppercase(self):
        self.name = self.name.upper()
        self.email = self.email.upper()
        return {"name": self.name, "email": self.email, "phone": self.phone}

    # 6. Write method to convert to lowercase
    #     - Inside this method, we need access to INSTANCE OBJECT
    def to_lowercase(self):
        self.name = self.name.lower()
        self.email = self.email.lower()
        return {"name": self.name, "email": self.email, "phone": self.phone}

print("#"*40, end="\n\n")
#########################

print("Release-4:")
print("-"*20)
# ---------------
# Inheritance
# EmployeeClassRelease4 is extending from EmployeeClassRelease3
# Whatever there in EmployeeClassRelease3 will come to EmployeeClassRelease4
class EmployeeClassRelease4(EmployeeClassRelease3):
    # 7. write method to get company details from CLASS OBJECT and
    #     store it in json file
    #     - Inside this method, we need access to CLASS OBJECT
    @classmethod
    def write_to_json(cls, json_file_path):
        # 1-way to get company details
        company_details = cls.get_company_details()
        # 2-way to get company details
        company_details = {"company_name": cls.company_name, "company_location": cls.company_location}

        my_json_file_handle = open(file=json_file_path, mode="w")
        import json
        json.dump(company_details, my_json_file_handle)
        my_json_file_handle.close()

    # 8. write method to get company details from json file
    #     - We DON'T need access to any of the object
    #         -- We DON'T need access to INSTANCE object
    #         -- We DON'T need access to CLASS object
    @staticmethod  # It will avoid passing class object or instance object
    def read_from_json(json_file_path):
        my_json_file_handle = open(file=json_file_path, mode="r")
        import json
        company_details = json.load(my_json_file_handle)
        my_json_file_handle.close()
        return company_details

print("#"*40, end="\n\n")
#########################

print("Testing Employee Class: 1st 2 methods")
print("-"*20)
# ---------------

EmployeeClassRelease4.store_company_details("XYZ Company", "XYZ Location")
# Internally, object 'Employee' will get passed to 1st argument 'cls'

company_details = EmployeeClassRelease4.get_company_details()
# Internally, object 'Employee' will get passed to 1st argument 'cls'
print("company_details:", company_details, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Testing Employee Class: methods 3 and 4")
print("-"*20)
# ---------------

e1 = EmployeeClassRelease4()
e2 = EmployeeClassRelease4()

# Store details
e1.store_employee_details("emp-1", "comp-1")
# Internally, object e1 will be passed to self
e2.store_employee_details("emp-2", "comp-2", 123456)

# Get details
print("Employee 1 Details:", e1.get_employee_details(), end="\n\n")
print("Employee 2 Details:", e2.get_employee_details(), end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Testing Employee Class: methods 5 and 6")
print("-"*20)
# ---------------

print("Employee 1 in upper case:", e1.to_uppercase())
# Internally e1 will be passed to self
print("Employee 1 in lower case:", e1.to_lowercase(), end="\n\n")
# Internally e1 will be passed to self

print("Employee 2 in upper case:", e2.to_uppercase())
# Internally e2 will be passed to self
print("Employee 2 in lower case:", e2.to_lowercase(), end="\n\n")
# Internally e2 will be passed to self

print("#"*40, end="\n\n")
#########################

print("Testing Employee Class: methods 7 and 8")
print("-"*20)
# ---------------

EmployeeClassRelease4.write_to_json("company_data.json")
# Internally object 'Employee' will be passed to 'cls'
print("company_data.json created. Please check")

company_details = EmployeeClassRelease4.read_from_json("company_data.json")
print("company_details:", company_details, end="\n\n")

print("#"*40, end="\n\n")
#########################


# class my_list(list):
#     pass