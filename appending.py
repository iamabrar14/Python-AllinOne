f=open('write.txt','a')
f.write(" "+"Appending a text using ")
f.close()
with open('write.txt','a') as f:
    f.write(" "+"If we use with keyword, we do not have to use close function")