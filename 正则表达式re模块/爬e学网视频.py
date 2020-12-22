import re
import requests

url = 'http://site2.rjkflm.com:666/index/index/view/id/1.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:83.0) Gecko/20100101 Firefox/83.0'}
response = requests.get(url=url, headers=headers)
if response.status_code == 200:
    video_url = re.findall('<source src="(.*?)" type="video/mp4">', response.text)[0]
    video_url = 'http://site2.rjkflm.com:666/' + video_url
    video_response = requests.get(url=video_url, headers=headers)
    if video_response.status_code == 200:
        data = video_response.content
        file = open('java视频.mp4', 'wb')
        file.write(data)
        file.close()
        print('下载成功！')