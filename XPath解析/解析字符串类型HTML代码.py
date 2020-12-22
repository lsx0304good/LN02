from lxml import etree

html_str = '"' \
           '<title>hahaha</title>' \
           '</head>' \
           '<body>' \
           '<img src="./请求模块requests/百度logo.png" />' \
           '</body></html>"'
html = etree.HTML(html_str)
html_txt = etree.tostring(html, encoding='utf-8')
print(html_txt.decode('utf-8'))
