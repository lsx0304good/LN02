import re

# 使用sub替换字符串
pattern = r'1[34578]\d{9}'
string = '中奖号码为：84978981 联系电话为：13611111111'
result = re.sub(pattern, '1XXXXXXXXXX', string)
print(result)

# 使用split分割字符串
pattern2 = r'[?|&]'
url = 'http://www.mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft"'
result = re.split(pattern2, url)
print(result)