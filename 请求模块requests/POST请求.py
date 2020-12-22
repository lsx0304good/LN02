import requests
import json

data = {
    '1': '能力是有限的，但努力是无限的',
    '2': '星光不问赶路人，时光不负有心人',
}
response = requests.post('http://httpbin.org/post', data=data)
response_dict = json.loads(response.text)
print(response_dict)
