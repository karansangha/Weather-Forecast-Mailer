import requests

def get_weather_forecast():
    url='http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=metric&appid=42c7c4285b12e98757f58c8a1bf99adc'

    #Open and read JSON
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    #Parse JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    #Create the forecast
    forecast = 'The Circus forecast for today is ' + description
    forecast += ' with a high of ' + str(temp_max) + 'C'
    forecast += ' and a low of ' + str(temp_min) + 'C'

    return forecast
