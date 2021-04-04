import requests
from bs4 import BeautifulSoup as BS

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
resp = requests.get('https://world-weather.ru/pogoda/russia/', headers=header).text
soup = BS(resp, 'html.parser')

for link in soup.find(class_="block-cities").find_all('a'):
print(link.text)
print(link.get('href'))

