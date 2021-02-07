from django.db import models

# Create your models here.
class Reg(models.Model):
    userid=models.CharField(max_length=6,primary_key=True)
    password=models.CharField(max_length=10)
    username=models.CharField(max_length=15)
    address=models.CharField(max_length=25)
    country=models.CharField(max_length=2)
    pincode=models.IntegerField()
    email=models.CharField(max_length=20)
    sex=models.CharField(max_length=6)
    language=models.CharField(max_length=2)
    about=models.CharField(max_length=100)
