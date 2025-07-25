"""This programm will separate even and odd numbers from a given list.
"""

def evenOdd(l):
    e=[]
    o=[]
    for num in l:
        if num%2==0:
            e.append(num)
        else:
            o.append(num)
    return e,o

a=int(input("How many numbers : "))
ls=[]
for i in range(a):
    x=int(input(f"Enter no {i+1} : "))
    ls.append(x)
even,odd=evenOdd(ls)
print("Original List : ",ls)
print("Even List : ",even)
print("Odd List : ",odd)