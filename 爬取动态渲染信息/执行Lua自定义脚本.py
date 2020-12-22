import requests
from urllib.parse import quote

lua_script = '''
function main(splash)
    splash:go("https://www.baidu.com/")
    splash:wait(0.5)
    return splash:html()
end
'''

splash_url = 'http://localhost:8050/execute?lua_source=' + quote(lua_script)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
response = requests.get(url=splash_url, headers=headers)
print(response.text)