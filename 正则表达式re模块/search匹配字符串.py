import re

# 获取第一个符合条件的
pattern = 'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.search(pattern, string, re.I)
print(match)
string = '项目名称MR_SHOP mr_shop'
match = re.search(pattern, string, re.I)
print(match)

# 可选匹配
pattern2 = '(\d?)+mrsoft\s?([\u4e00-\u9fa5]?)+'
# 数字可有可无，空格可有可无，汉字可有可无
match = re.search(pattern2, '01mrsoft')
print(match)
match = re.search(pattern2, 'mrsoft')
print(match)
match = re.search(pattern2, 'mrsoft ')
print(match)
match = re.search(pattern2, 'mrsoft 第一')
print(match)
match = re.search(pattern2, 'rsoft 第一')  # 不匹配，因为不包含完整mrsoft
print(match)

# 匹配字符串边界
pattern3 = r'\bmr\b'  # r表示\b不能转义
match = re.search(pattern3, 'mrsoft')  # None
print(match)
match = re.search(pattern3, 'mr soft')
print(match)
match = re.search(pattern3, 'mrsoft ')  # None
print(match)
match = re.search(pattern3, 'mr.soft')
print(match)

