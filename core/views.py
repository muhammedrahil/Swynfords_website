from django.shortcuts import render,redirect
import threading
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import *
import datetime
# Create your views here.


def index(request):
  # visited(request,"index") 
  return render(request, 'index.html')


def mail_send(request,mail_data):
  current_site = get_current_site(request)
  mail_subject = "New request for client"
  massage = render_to_string('layout/verification-email.html',
      {
      "from": mail_data.get("email"),
      "name": mail_data.get('name'),
      'domain'  : current_site,
      "subject" : mail_data.get('subject')
  })
  to_email="SwynfordsPvtLtd@gmail.com"
  send_email = EmailMessage(mail_subject,massage,to=[to_email])
  send_email.send()
  return print("Successfully sent")


def contact(request):
  if request.method == 'POST':
    mail_data = {"name" : request.POST.get('name',None) ,
                 "email" :request.POST.get('email',None) ,
                 "subject" : request.POST.get('subject',None),
                 "message" : request.POST.get('message',None),
                 "created_at": datetime.datetime.now()}
    email = Email.objects.create(**mail_data)
    my_thread = threading.Thread(target=mail_send,args=(request,mail_data))
    my_thread.start()
    messages.success(request,'Sent message Successfully')
    return redirect("contact")
  # visited(request,"contact")
  return render(request, 'contact.html')

def about(request):
  # visited(request,"about")
  return render(request, 'about.html')



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def visited(request,page_name):
  Visted_site.objects.create(page=page_name+" page",domain=get_client_ip(request),created_at=datetime.datetime.now())