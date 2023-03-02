from django.shortcuts import render
from django.core.mail import EmailMessage
import threading

# Create your views here.


def index(request):
  return render(request, 'index.html')


def mail_send(mail_data):
  def send(mail_data):
    email = EmailMessage(
        mail_data.get('subject',None),
        mail_data.get('message',None),
        'from@example.com',
        ['to@example.com'],
        headers={'Message-ID': 'foo'},
    )
    email.send()
    return "Successfully sent"
  my_thread = threading.Thread(target=send(mail_data))
  my_thread.start()
  return "Successfully sent"


def contact(request):
  if request.method == 'POST':
    mail_data = {"name" : request.POST.get('name',None) ,
                 "email" :request.POST.get('email',None) ,
                 "subject" : request.POST.get('subject',None),
                 "message" : request.POST.get('message',None)}
    mail_send(mail_data)
  return render(request, 'contact.html')

def about(request):
  
  return render(request, 'about.html')
