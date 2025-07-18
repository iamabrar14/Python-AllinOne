import win32com.client

# Initialize the speaker using SAPI
speaker = win32com.client.Dispatch("SAPI.SpVoice")


a=[]
x=int(input("How many names : "))
for names in range(x):
    b=input(f"Enter name {names+1} : ")
    a.append(b)

#Main code
for name in a:
    text = f"Hi,  My name is  {name}"
    print(text)  # Optional, for display
    speaker.Speak(text)


