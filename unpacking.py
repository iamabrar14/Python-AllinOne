info = ['Alice', 25, 'Engineer', 'Dhaka', 'Bangladesh']
a, _, b, _, _ = info
print(a)  
print(b) 
a,*b=info
print(a)
print(*b)
