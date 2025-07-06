l=[1,2,3,4,5,6,7,8,9,10]
newl=list(filter(lambda x: x%2==0,l)) #only prints even number
print("Old list : ",l)
print("New list(only even numbers) : ",newl)