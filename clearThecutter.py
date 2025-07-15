import os

files=os.listdir(r"C:\Users\zoom\Pictures\Screenshots")
i=1
for file in files:
    if file.endswith(".png"):  #finding png files in a specific folder.
     print(file)
     os.rename(f"C:\\Users\\zoom\\Pictures\\screenshots\\{file}",f"C:\\Users\\zoom\\Pictures\\screenshots\\{i}.png")
     i=i+1 
     #Renaming every png files
    