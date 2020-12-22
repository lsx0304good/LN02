import requests

response = requests.get('https://www.baidu.com/img/bd_logo1.png?where=super')
print(response.content)  # 打印二进制数据
with open('百度logo.png', 'wb') as f:
    f.write(response.content)
