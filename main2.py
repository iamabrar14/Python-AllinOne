import maths as m 

a=input("Press s for sum,u for sub, m for multi and d for div : ").strip().lower()
x=int(input("Enter first number : "))
y=int(input("Enter second number: "))

if (a=='s'):
    m.plus(x,y)
elif(a=='u'):
    m.minus(x,y)
elif(a=='m'):
    m.mul(x,y)
elif(a=='d'):
    m.div(x,y)
else:
    print("Wrong input")
    