class Employee:
    def getsalary(self):
        return 20000          #Parent Class
class Manager(Employee):
    def getsalary(self):      #Method Overriding
        return 35000
class CEO(Employee):
    def getsalary(self):     #Method Overriding
        return 60000
e=Employee()
m=Manager()
c=CEO()
print("Salary of this employee : ",e.getsalary())
print("Salary of this Manager : ",m.getsalary())
print("Salary of the CEO : ",c.getsalary())
#In method overriding, the child class redefines the parent class method to customize its behavior.

