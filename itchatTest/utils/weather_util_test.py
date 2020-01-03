from bs4 import BeautifulSoup
import requests


html = requests.get('http://tianqi.hao123.com/shenzhen.html').content
soup = BeautifulSoup(html, 'lxml', from_encoding='utf-8')
date = soup.find('div', class_='slide-item').find('div', class_='temp').get_text()
weather = soup.find('div', class_='slide-item').find('div', class_='weather').get_text()
wind = soup.find('div', class_='slide-item').find('div', class_='wind').get_text()
print(date,weather,wind)
