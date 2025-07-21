import requests

data = {
    'title': 'My Post',
    'body': 'This is a test post.',
    'userId': 1
}

response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.status_code)
print(response.json())
