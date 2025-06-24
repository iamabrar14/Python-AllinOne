person={
    "Name":"Abrar",
    "Age":24,
    "email":"iamabrar14@gmail.com"
    
}

print(person["Name"])
""" Another way of declaring a dictionary
"""
a=dict(name="Anik", age=24,email="Anikmahamud@gmail.com")
print(a["name"])
#Adding and Updating
person["Blood Group"]="A+"
"""
del person["Age"] for deleting a value
"""
a["Blood Group"]="O+"
print(person)
print(a)