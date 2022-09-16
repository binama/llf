from django.template. loader import render_to_string
from django.utils.html import strip_tags
from django.core import mail



def send_code_email(user):
    context = {
        'text_detail': 'Спасибо за регистрацию!',
        'email': user.email,
        'domain': 'localhost',
        'activation_code': user.activation_code
    }

    msg = render_to_string('email.html', context)
    plain_message = strip_tags(msg)
    subject = 'Activate account'
    to = user.email
    mail.send_mail(subject, plain_message, 'binama81@gmail.ru', [to,], html_message=msg)