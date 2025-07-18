import time
print("Instantly Printed")
time.sleep(4)
print("Printed after 4 second")

#This will print current time but in formatted way using time.strftime
t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)