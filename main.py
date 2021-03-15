import requests
from bs4 import BeautifulSoup


def getWeather():
    print('Type a City name:')
    city_input = str(input())

    url = f'https://google.com/search?q=weather {city_input}'
    r = requests.get(url)
    s = BeautifulSoup(r.text, 'html.parser')

    location = s.find('span', class_='BNeawe').text
    weather = s.find('div', class_='BNeawe tAd8D AP7Wnd').text
    temperature = s.find('div', class_='BNeawe').text

    print(location)
    print(temperature)
    print(weather)

    return location, temperature, weather
