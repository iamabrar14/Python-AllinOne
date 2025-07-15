import os

files=os.listdir(r"C:\Users\zoom\Pictures\Screenshots(2)")
i=1
for file in files:
    if file.endswith(".pf"):  #finding png files in a specific folder.
     print(file)
     os.rename(f"C:\\Users\\zoom\\Pictures\\screenshots(2)\\{file}",f"C:\\Users\\zoom\\Pictures\\screenshots(2)\\{i}.png")
     i=i+1 
     #Renaming every png files
    