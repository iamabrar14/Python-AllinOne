"""The requests module in Python is a third-party library used to make HTTP requests easily. It 
allows your Python programs to communicate with websites, 
APIs, or any online resources over HTTP/HTTPS protocols.
"""
import requests
response=requests.get("https://github.com/iamabrar14")
print(response.text) #It will print the code of that following website