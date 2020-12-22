import requests

# URL传参
response = requests.get('http://httpbin.org/get?name=Simon&age=24')
print(response.text)

# params传参
params = {'name': 'Simon', 'age': 24}
response2 = requests.get('http://httpbin.org/get', params=params)
print(response2.text)