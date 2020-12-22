import requests

for a in range(0, 50):
    try:
        response = requests.get('https://www.baidu.com/', timeout=0.1)
        print(response.status_code)
    except Exception as e:
        print('异常' + str(e))
