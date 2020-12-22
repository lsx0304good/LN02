from requests_html import HTMLSession, UserAgent

session = HTMLSession()
ua = UserAgent().random
r = session.get('http://httpbin.org/get', headers={'user-agent': ua})
if r.status_code == 200:
    print(r.text)
