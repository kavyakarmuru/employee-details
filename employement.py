# Defined a Employee class with attributes of employee.
class Employee():
    def __init__(self,name,ID,title,department):
        self.name=name
        self.ID=ID
        self.title=title
        self.department=department
    def display(self):
        employee_details={}
        employee_details[self.department]=(self.name,self.ID,self.title)
        return employee_details 
# Defined the Department class and inherited Employee class. 
class Department(Employee):
    def __init__(self,name,ID,title,department,employees={}):
        super().__init__(name,ID,title,department)
# Returned the display function in Employee class to a parameter employees.
        self.employees=Employee.display(self)
# Define the method to add employee from the employees dictionary.
    def __add__(self,v1,v2):
        if(v2 not in self.employees.values()):
            self.employees[v1]=v2
        else:
            return("Employees details already exists.")
# Define the method to remove employee from the employees dictionary. 
    def __remove__(self,v1,v2):
        if(v2 in self.employees.values()):
            del self.employees[v1] 
        else:
            return("The employee details your searching not prsent.")
# Defioned the class to display employee details of the particular department.
    def get_details(self):
        return self.employees
d1=Department('Alekya',456,'System engineer','IT')
d2=Department('Rosha',376,'Manager','Finance')
d3=Department('Nikhi',267,'HR','Human resource')
d1.__add__('HR',('Shoba',673,'Senior manager'))
print(d1.get_details())
print(d2.__remove__('Finance',('kanchana',367,'Manager')))
print(d3.get_details())