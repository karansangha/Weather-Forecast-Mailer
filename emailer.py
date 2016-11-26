emails = {}

try:
    email_file = open('emails.txt', 'r')

    for line in email_file:
        (email, name) = line.split(',')
        emails[email] = name.strip()

except FileNotFoundError as err:
    print(err)

print (emails)

try:
    schedule_file = open('schedule.txt', 'r')
    schedule = schedule_file.read()

except FileNotFoundError as err:
    print(err)

print (schedule)
