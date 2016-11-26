import requests
import smtplib

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

    return forecast

def send_emails(emails, schedule, forecast):
    #Connect to the smpt server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    #Start TLS encrpytion
    server.starttls()

    from_email = 'dbzs.110mb@gmail.com'
    password = input("What's your password?")
    server.login(from_email, password=password)

    for to_email, name in emails.items():
        message = 'Subject: Welcome to the Circus!\n'
        message += 'Hi '+ name + '!\n'
        message += forecast + '\n'
        message += schedule + '\n'
        message += 'Hope to see you there!!'
        server.sendmail(from_email, to_email, message )

    server.quit()

def main():
    emails = get_emails()
    print (emails)

    schedule = get_schedule()
    print (schedule)

    forecast = get_weather_forecast()
    print(forecast)

    send_emails(emails, schedule, forecast)

main()
