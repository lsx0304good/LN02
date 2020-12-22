from lxml import etree

parser = etree.HTMLParser()
html = etree.parse('demo.html', parser=parser)
html_txt = etree.tostring(html, encoding='utf-8')
print(html_txt.decode('utf-8'))