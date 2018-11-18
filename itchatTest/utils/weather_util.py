from bs4 import BeautifulSoup
import requests

def get_weather_today():
    html = requests.get('http://tianqi.cncn.com/shenzhen').content
    soup = BeautifulSoup(html,'lxml', from_encoding='utf-8')
    result = soup.find('div', class_='txt_share').find('li').get_text()
    return result