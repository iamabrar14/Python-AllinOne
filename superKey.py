#The super keyword in python is used to refer to the parent class.
#It is important when a class inherits from multiple parent class.
class ParentClass:
    def parentMethod(self):
        print("This is the parent method")
        
class ChildClass(ParentClass):
    def childMethod(self):
        print("This is the child method")
        super().parentMethod() #Using a method from parent class
obj=ChildClass()
obj.childMethod()