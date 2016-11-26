import requests

def get_emails():


    emails = {}

    try:
        email_file = open('emails.txt', 'r')

        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except FileNotFoundError as err:
        print(err)

    return emails

def get_schedule():

    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()

    except FileNotFoundError as err:
        print(err)

    return schedule

def get_weather_forecast():
    url='http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=metric&appid=42c7c4285b12e98757f58c8a1bf99adc'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    # print (weather_json)

    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']
    # print (description)
    # print (temp_min, temp_max)

    forecast = 'The Circus forecast for today is ' + description
    forecast += ' with a high of ' + str(temp_max) + 'C'
    forecast += ' and a low of ' + str(temp_min) + 'C'

    print (forecast)

def main():
    emails = get_emails()
    print (emails)

    schedule = get_schedule()
    print (schedule)

    get_weather_forecast()

main()
