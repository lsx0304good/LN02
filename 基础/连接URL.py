import urllib.parse

base_url = 'https://docs.python.org'
# 第二参数不完整时
print(urllib.parse.urljoin(base_url, '3/library/urllib.parse.html'))
# 第二参数完整时
print(urllib.parse.urljoin(base_url, 'https://docs.python.org/3/library/urllib.parse.html#url-parsing'))