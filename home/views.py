from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def email(request):
    subject='Thank you for registering to our site'
    message='We are very much happy to include you as our mamber'
    email_from=settings.EMAIL_HOST_USER
    recipient_list=['gkdaslab@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    text='<H1>Your message has been sent to gkdaslab</H1>'
    return HttpResponse(text)
