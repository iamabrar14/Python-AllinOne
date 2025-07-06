with open ('nex.txt','r') as f:
    f.seek(9) #Skips till 9 character
    #Seek helps to forward point and skip bytes as per parameter.
    print(f.tell()) #Tells us about skipping point
    data=f.read(5)
    print(data) #prints characters after skipping point
  