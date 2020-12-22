import requests

bd = open('百度logo.png', 'rb')
file = {'file': bd}
response = requests.post('http://httpbin.org/post', files=file)
print(response.text)