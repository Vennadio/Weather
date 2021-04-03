import requests
from bs4 import BeautifulSoup as BS


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
resp = requests.get('https://world-weather.ru/pogoda/russia/moscow/24hours/', headers=header).text
soup = BS(resp, 'html.parser')
weather = soup.find_all('table', class_= "weather-today")
for data in weather:
    if data.find('td', class_ = 'weather-feeling' ):
        print (data)

#title = soup.find('table', class_='day hourly-1').text

#print(title.strip())
#print(weather)


