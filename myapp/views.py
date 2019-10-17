from django.shortcuts import render
from django.views.generic import FormView
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings




# Create your views here.

class EmailView(FormView):
    template_name='myform.html'
    form_class=EmailForm
    success_url='success'

    def form_valid(self, form):
        self.send_email(form)
        return super().form_valid(form)

    def send_email(self, form):
        subject="Mail from drylab"
        message = "You have successfully registered your name in our database"
        email_from=settings.EMAIL_HOST_USER
        recipient_list=[form.cleaned_data['email']]
        send_mail(subject, message, email_from, recipient_list)
        pass
