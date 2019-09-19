from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=80)
    last_name =models.CharField(max_length=80)
    email =models.CharField(max_length=80)
    hashed_pwd = models.CharField(max_length=300)
    salt = models.CharField(max_length=40, default="spacecowboy")
    created_on=models.DateTimeField(auto_now_add=True)
