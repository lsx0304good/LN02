import re

# 匹配指定字符
pattern = 'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.findall(pattern, string, re.I)
print(match)
string = '项目名称MR_SHOP mr_shop'
match = re.findall(pattern, string)
print(match)

# 贪婪匹配
pattern2 = 'https://(.*)/'
pattern3 = 'https://.*/'
match = re.findall(pattern2, 'https://www.hao123.com/')
print(match)
match = re.findall(pattern3, 'https://www.hao123.com/')
print(match)

# 非贪婪匹配
pattern4 = 'https://.*?(\d+).com/'
match = re.findall(pattern4, 'https://www.hao123.com/')
print(match)