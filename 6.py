#branching- using if-----elif

x=int(input("Enter your score : "))

if x>=80:
    print("A+")
elif x>=70:
    print("A")
elif x>=60:
    print("A-")
elif x>=50:
    print("B")
elif x>=40:
    print("C")
elif x>=33:
    print("D")
else:
    print("Failed")