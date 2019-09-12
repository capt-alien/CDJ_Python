from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state= models.CharField(max_length=2)
    description=models.CharField(max_length=255, default="very old")


class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
