from django.db import models

# Create your models here.



class Email(models.Model):
  email = models.CharField(max_length=255,blank=True,null=True)
  name = models.CharField(max_length=255,blank=True,null=True)
  subject = models.CharField(max_length=255,blank=True,null=True)
  message = models.TextField(blank=True,null=True)
  created_at = models.DateTimeField(max_length=255,blank=True,null=True)
  


class Visted_site(models.Model):
  page  = models.CharField(max_length=255,blank=True,null=True)
  created_at = models.CharField(max_length=255,blank=True,null=True)
  domain = models.CharField(max_length=255,blank=True,null=True)

