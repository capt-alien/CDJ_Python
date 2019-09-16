from django.db import models



# Create your models here.



class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)
    notes=models.TextField(blank=True)


class Books(models.Model):
    title= models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.TimeField(auto_now=True)
    updated_at = models.TimeField(auto_now=True)
    authors = models.ManyToManyField(Authors, default="Mr. Dough")
