import urllib.parse

list_url = ['https', 'docs.python.org', '/3/library/urllib.parse.html', '', '', '']
tuple_url = ('https', 'docs.python.org', '/3/library/urllib.parse.html', '', '', '')
dict_url = {'scheme': 'https',
            'netloc': 'docs.python.org',
            'path': '/3/library/urllib.parse.html',
            'params': '',
            'query': '',
            'fragment': '', }

# 方法一：urlunparse
print('组合列表类型的URL:', urllib.parse.urlunparse(list_url))
print('组合元组类型的URL:', urllib.parse.urlunparse(tuple_url))
print('组合字典类型的URL:', urllib.parse.urlunparse(dict_url.values()))

# 方法二：urlunsplit 必须是五个参数！！！！ 没有param
list_url = ['https', 'docs.python.org', '/3/library/urllib.parse.html', '', '']
tuple_url = ('https', 'docs.python.org', '/3/library/urllib.parse.html', '', '')
dict_url = {'scheme': 'https',
            'netloc': 'docs.python.org',
            'path': '/3/library/urllib.parse.html',
            'query': '',
            'fragment': '', }
print('组合列表类型的URL:', urllib.parse.urlunsplit(list_url))
print('组合元组类型的URL:', urllib.parse.urlunsplit(tuple_url))
print('组合字典类型的URL:', urllib.parse.urlunsplit(dict_url.values()))
