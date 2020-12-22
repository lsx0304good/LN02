from requests_html import HTMLSession

session = HTMLSession()

# GET
url = 'http://news.youth.cn/'
r1 = session.get(url)
print(r1.html)

# POST
data = {'user': 'admin', 'password': 123456}
r2 = session.post('http://httpbin.org/post', data=data)
if r2.status_code == 200:
    print(r2.text)