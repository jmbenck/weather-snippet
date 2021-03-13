# Weather extraction snippet

This is an example of how we can use Python and Web Scraping to get information making search from a webpage.

We will make a search on Google for the weather of a given City and use BeautifulSoup to extract that data.

We know there are better ways for getting weather information (like API's). But I think this is a nice snippet for demonstration purposes.
## Dependencies
We'll use Requests and BeautifulSoup modules.
````Python3
pip install requests
pip install beautifulsoup4
````
or you could just install all dependencies from ``requirements.txt``

````Python3
pip install -r requirements.txt
````

## Code Step-by-Step
### Import the modules

````Python3
import requests
from bs4 import BeautifulSoup
````

### Building the url search
We can make a Google search with ``GET`` method passing the query in the url:

````Python3
search = 'Weather in Foz do Iguaçu'
url = 'https://google.com/search?&q={}'.format(search)
````
The ``search`` variable represents the query we want for getting an specific city weather.

### Making request
````Python3
r = requests.get(url)
````
The ``request.get`` method will make a ``GET`` request for the given URL and store the response in the ``r`` variable.


### Reading in BeautifulSoup
````Python3
s = BeautifulSoup(r.text, 'html.parser')
````
We create an BeautifulSoup object with the response. The ``html.parse`` will structure the response as HTML document, so we could make searches.


### Getting Data
Now in the variable ``s`` we have structured html page that we could search in.

Analysing a page with a given search We can see where is the code for the infomation we want.
````html
...
<!-- Location -->
<span class="BNeawe tAd8D AP7Wnd">Foz do Iguaçu, State of Paraná</span>
...
<!-- Temperature -->
<div class="BNeawe iBp4i AP7Wnd">23°C</div>
...
<!-- Local time and Weather conditions -->
<div class="BNeawe tAd8D AP7Wnd">Friday 21:55 
    Clear with periodic clouds
</div>
...
````
Example of a page with weather information from Foz do Iguaçu (city from Brazil).

You can see the HTML code with the browser inspector, just remember to **disable Javascript** since BeautifulSoup don't process the js files.

### Getting Location
````Python3
location = s.find('span', class_='BNeawe').text
print(location)
# OUTPUT: 
# Foz do Iguaçu, State of Paraná
````
The ``find`` method from beautiful soup will search the ``span`` element with the class name ``BNeawe``.

### Getting Temperature info
````Python3
temperature = s.find('div', class_='BNeawe').text
print(temperature)
# OUTPUT: 
# 23°C

````
The ``find`` method from beautiful soup will search for the first element ``div`` element with the class name ``BNeawe``.

### Getting Weather conditions
````Python3
weather = s.find('div', class_='BNeawe tAd8D AP7Wnd').text
print(weather)
# OUTPUT: 
# Friday 21:55 
# Clear with periodic clouds
````
The ``find`` method from beautiful soup will search for the first element ``div`` element with the class name ``BNeawe tAd8D AP7Wnd``.
>Note that we also get the local time and day of week of the city in this div, witch is pretty nice tho.

## Run the sample code
The ``main.py`` is a demonstration where you run and give and input with a City name to get the results.

````Python3 
pip install -r requirements.txt
python main.py
````

## Contribute
That's all. Feel free for collaborating with this repo. Thank you.
