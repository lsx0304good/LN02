import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}
quotes_list = []

for i in range(1, 11):
    url = 'http://quotes.toscrape.com/page/{}/'.format(i)
    response = requests.get(url, headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features='lxml')
        text_all = soup.find_all('span', class_='text')
        quotes_list.extend(text_all)

txt_file = open('data.txt', 'w', encoding='utf-8')
for i, value in enumerate(quotes_list):
    txt_file.write(str(i) + value.text + '\n')
txt_file.close()