from django.urls import path
from . import views as v

urlpatterns = [
    path('',v.index,name='index'),
    path('contact/',v.contact,name='contact'), 
    path('about/',v.about,name='about'),
    
]