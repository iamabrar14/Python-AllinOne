"""We will see how to use class method as an alternative constructor
"""
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("--")[0],int(string.split("--")[1]))
e1=Employee("Abrar",15000)
print(e1.name)
print(e1.salary)
string="Anik--20000"
e2=Employee.fromStr(string)
print(e2.name)
print(e2.salary)
"""Data can come in many form. By using this class method, we actually converted the string and 
sent it to main constructor
"""