import requests

def load_get():
    r = requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
    print('URL:',r.url)
    print('Header:',r.headers)
    print('StatusCode',r.status_code)
    print('Text:',r.text)

def get_json():
    r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
    print("Json:",r.json())
if __name__ == 'main':
    load_get()