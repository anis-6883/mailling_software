from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
import os

def home(request):

    if request.method == 'POST':
        EMAIL_HOST_USER = os.environ.get('EMAIL_USER')

        subject  = request.POST.get('subject', '')
        email_id = request.POST.get('email', '')
        message  = request.POST.get('message', '')
        email    = EmailMessage(subject, message, EMAIL_HOST_USER, [email_id])
        email.content_subtype = 'html'

        if request.FILES.get('file'):
            file = request.FILES['file']
            email.attach(file.name, file.read(), file.content_type)

        email.send()

        return redirect('/')
        
    else:
        return render(request, 'sender/index.html')