import smtplib
from email.message import EmailMessage

#Login ID and Password of your email
username = 'email_id'
password = 'password'

try:
    data = EmailMessage()

    # senders email address and recipients email address
    data['From'] = 'studyhacks@example.com'
    data['To'] = 'abc@example.com'

    # subject of email
    data['Subject'] = 'This is subject'

    # The content file consist of the body of your message
    with open('content.txt') as file:
        data.set_content(file.read())

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.send_message(data)
    server.quit()

    print("🙂 Email to  '%s'  is sent successfully 🙂 " %data['To'])

except:
    print("Sorry ☹ Email to  '%s'  is Failed" %data['To'])


