import os

files=os.listdir(r"C:\Users\zoom\Pictures\Screenshots")
for file in files:
    if file.endswith(".png"):
     print(file)
     #finding png files in a specific folder.