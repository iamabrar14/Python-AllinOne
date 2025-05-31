numbers=[1,2,3]
chars=['A','B','C']
print("Outside Loop")
for number in numbers:
    print("Inside Number Loop")
    for char in chars:
        print("Inside Char Loop")
        print(number,char)