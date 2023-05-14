from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail, EmailMessage

def sendemail(request):
    email_subject = 'Welcome'
    message2 = render_to_string("email.html", {
        'name': 'There',
    })
    email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        ['legacyallan0@gmail.com'],
    )
    email.fail_silently = False
    return  email.send()