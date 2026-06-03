"""
In this program, we are implementing below 2 methods

5. Write method to convert to uppercase
    - Inside this method, we need access to INSTANCE OBJECT

6. Write method to convert to lowercase
    - Inside this method, we need access to INSTANCE OBJECT
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

print("Testing Employee Class: 1st 2 methods")
print("-"*20)
# ---------------

Employee.store_company_details("XYZ Company", "XYZ Location")
# Internally, object 'Employee' will get passed to 1st argument 'cls'

company_details = Employee.get_company_details()
# Internally, object 'Employee' will get passed to 1st argument 'cls'
print("company_details:", company_details, end="\n\n")

print("#"*40, end="\n\n")
#########################

print("Testing Employee Class: methods 3 and 4")
print("-"*20)
# ---------------

e1 = Employee()
e2 = Employee()

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