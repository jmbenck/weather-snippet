# Weather extraction snippet
[![Build Status](https://travis-ci.com/jmbenck/weather-snippet.svg?branch=master)](https://travis-ci.com/jmbenck/weather-snippet)

This is an example of how we can use Python and [Web Scraping](https://bit.ly/3qOY5Pa) to get specific information by making a search on a webpage.

We will make a search on Google for the weather of a given city and use [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) to extract that data.

We know there are better ways for getting weather information (like API's). But I think this is a nice snippet for demonstration purposes.

## Tests
For learning purposes, this repo is using [Travis CI](https://www.travis-ci.com/). The file [``test_.py``](https://github.com/jmbenck/weather-snippet/blob/master/test_.py) uses the 20 biggest cities to test the program and, with Regex, check if the response is as expected.

## Dependencies
Install Requests and BeautifulSoup modules.
````Python3
pip install requests
pip install beautifulsoup4
````
or you could just install all dependencies from ``requirements.txt``.

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
We can make a Google search using the HTTP ``GET`` method by passing a ``search`` parameter and ``q`` value for the query in the ``url``.

````Python3
city = 'Foz-do-Iguaçu'
url = 'https://google.com/search?&q=weather {}'.format(city)

# url = 'https://google.com/search?&q=weather-Foz-do-Iguaçu'
````

The ``city`` variable represents the value that we will append to the url parameter.


### Making request
````Python3
r = requests.get(url)
````
The ``request.get`` method will make a ``GET`` request to the given URL and store the response in the ``r`` variable.

So, the ``r`` value will be the raw ``HTML`` content resulting from the url search.


### Reading in BeautifulSoup
````Python3
s = BeautifulSoup(r.text, 'html.parser')
````
We create a BeautifulSoup object with the ``r`` variable. 

The ``html.parse`` will structure the response as ``HTML`` document. Then, we can navigate thought the elements using [DOM (Document Object Model)](https://www.w3schools.com/whatis/whatis_htmldom.asp).


### Getting Data
Now in the variable ``s`` we have structured html page that we can search in using DOM.

Let's take a look at the ``HTML`` resulting from this url ``https://google.com/search?&q=weather-Foz-do-Iguaçu ``

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

>Note: You can see the ``HTML`` code with the ``browser inspector``. Just remember to **disable Javascript** since BeautifulSoup **don't** process the js files, and it can change some attributes in the page.

Analysing the page is possible to locate where is the information we want to extract. Then, We have will use the ``elements``, and the ``classes names`` to make our search.
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
The ``main.py`` is a demonstration code where you give input with a City name to get the results.

````Python3 
pip install -r requirements.txt
python main.py
````

## Contribute
That's all. Feel free for collaborating with this repo. Thank you.
