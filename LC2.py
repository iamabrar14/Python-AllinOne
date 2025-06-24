evens=[x for x in range(10) if x%2==0]
print(evens)
labels=["Even" if x%2==0 else "Odd" for x in range(10)]
print(labels)
#First one will print all the even numbers from 1-10
#Second one will label the numbers even or odd