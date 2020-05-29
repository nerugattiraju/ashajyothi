from django.db import models


class Content1(models.Model):
    Name= models.CharField(max_length=300)
    Email=models.EmailField(unique=True)
    Massage=models.TextField()
class Document(models.Model):
    description = models.CharField(max_length=255,blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
class Simple(models.Model):
    myfile=models.FileField()
class Data(models.Model):
    data=models.TextField()
class Catch(models.Model):
    image=models.CharField(max_length=255)
class Files(models.Model):
    image=models.CharField(max_length=225)