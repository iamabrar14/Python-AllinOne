numbers = []
course=int(input("How many courses : "))
print("Enter your marks of courses :")

for i in range(course):
    num = int(input(f"Course {i+1}: "))
    numbers.append(num)
    
total=sum(numbers)
avrg=total/course
if avrg>=80:
    cgpa=4.00
elif avrg>=70:
    cgpa=3.75
elif avrg>=60:
    cgpa=3.00
elif avrg>=50:
    cgpa=2.75
elif avrg>=40:
    cgpa=2.50
elif avrg>=33:
    cgpa=2.00
else:
    cgpa="Invalid"    
print("Your marks :", numbers)
print("total : ",total)
print("average marks  : ",avrg)
print("CGPA: ",cgpa)
