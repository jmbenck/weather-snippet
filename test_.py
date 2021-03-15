import main
import pytest
import re


# 0 City name has a ',' char
# 1 Temperature has num and symbol(º)
# 2 Weather conditions has pattern '00:00'

# Input of 20 biggest cities
@pytest.mark.parametrize('city', ['Buenos Aires ', 'Calcutá', 'Los Angeles ', 'Bangkok ', 'Moscou ', 'Cairo ', 'Osaka-Kobe-Kyoto ', 'Dkaka ', 'Pequim ', 'Guangzhou-Foshan ', 'Cidade do México ', 'São Paulo ', 'Nova York ', 'Xangai ', 'Mumbai ', 'Seul ', 'Manila ', 'Deli ', 'Jacarta ', 'Tóquio '])
def test_function_1(city):
    # Override the Python built-in input method
    main.input = lambda: city
    # Call the function you would like to test (which uses input)
    output = main.getWeather()
    assert re.findall(r',', output[0]) != ''
    assert re.findall(r'°', output[1]) != ''
    assert re.findall(r'\d+:\d+', output[2]) != ''
