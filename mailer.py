import smtplib

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
        message += 'Hi '+ name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n\n'
        message += 'Hope to see you there!!'
        server.sendmail(from_email, to_email, message )

    server.quit()
