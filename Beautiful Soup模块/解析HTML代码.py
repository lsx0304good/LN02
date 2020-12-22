from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
<title>this is the title</title>
</head>
<body>
<p>this is the body</p>
<p>this is the title</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, features='lxml')
print('head:', soup.head)
print('body:', soup.body)
print('title:', soup.title)
print('p:', soup.p)