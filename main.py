import requests
from bs4 import BeautifulSoup


def getWeather(city):
    search = city
    url = f'https://google.com/search?&q=Weather in {search}'

    r = requests.get(url)

    s = BeautifulSoup(r.text, 'html.parser')

    location = s.find('span', class_='BNeawe').text
    print(location)

    temperature = s.find('div', class_='BNeawe').text
    print(temperature)

    weather = s.find('div', class_='BNeawe tAd8D AP7Wnd').text
    print(weather)


city = str(input())
getWeather(city)