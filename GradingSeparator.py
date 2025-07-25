def sep(l):
    Aplus=[]
    onlyA=[]
    Aminus=[]
    B=[]
    C=[]
    D=[]
    F=[]
    for number in l:
        if number>=80:
            Aplus.append(number)
        elif number>=70 and number<80:
            onlyA.append(number)
        elif number>=60 and number<70:
            Aminus.append(number)
        elif number>=50 and number<60:
            B.append(number)
        elif number>=40 and number<50:
            C.append(number)
        elif number>=33 and number<40:
            D.append(number)
        else:
            F.append(number)
    return Aplus,onlyA,Aminus,B,C,D,F
        
            
x=int(input("How many students marks you want to enter : "))
numbers=[]
for i in range(x):
    marks=int(input(f"Enter student no {i+1} mark : "))
    numbers.append(marks)
    
Aplus,A,Aminus,b,c,d,f=sep(numbers)
print("A+",Aplus)
print("A",A)
print("A-",Aminus)
print("B",b)
print("C",c)
print("D",d)
print("Failed",f)
