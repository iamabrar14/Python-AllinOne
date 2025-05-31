#Basic calculations
num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))

sum=num1+num2
multi=num1*num2
if num1>num2:
    div=num1/num2
    sub=num1-num2
    print("Substraction is : ",sub)
    print("Division is : ",div) 
else:
    print("Division is not possible")
    print("Substraction is not possible")

print("Summation is: ",sum)
print("Multiplication is : ",multi)


