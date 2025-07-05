"""We can open a txt or bin file in python using open() function. It takes two arguement: firstly
'file name' and second 'mode'. r for read, w for write and a for append
"""
f=open('myfile.txt','r')
text=f.read()
print(text)
f.close()