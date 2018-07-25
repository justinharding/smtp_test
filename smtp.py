import smtplib

# smtp_server = 'smtp.gmail.com'
smtp_server = 'smtp.office365.com'
smtp_port = 587

# gmail_user = ""
# gmail_password = ""

sent_from = ''
to = ['']
subject = "what sort of a message is this"
body = "this is a test message to see if it works"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    print('about to construct')
    s = smtplib.SMTP(smtp_server, smtp_port)

    print('about to starttls')
    s.starttls()

    print 'about to login'
    s.login(gmail_user, gmail_password)

    print 'about to sendmail'
    s.sendmail(sent_from, to, email_text)

    print 'about to close'
    s.close()

    print 'Email sent'

except Exception as e:
    print "something broke"
    print(e)


