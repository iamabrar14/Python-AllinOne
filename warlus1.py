#Warlus operator allows us to assign value to a variable within an expression
numbers=[1,2,3,4,5]
while(n:=len(numbers))>0:
    print(numbers.pop())
