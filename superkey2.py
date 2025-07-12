class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id) #using constructor of parent class directly
        self.lang=lang
obj=Programmer("Abrar","05","Python")
obj2=Programmer("Kamrul","01","Dart")
print(f"Name: {obj.name}, id {obj.id} and language: {obj.lang}")
print(f"Name: {obj2.name}, id {obj2.id} and language: {obj2.lang}") 