from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=80)
    last_name =models.CharField(max_length=80)
    email =models.CharField(max_length=80)
    hashed_pwd = models.CharField(max_length=300)
    # salt = models.CharField(max_length=40, default="spacecowboy")
    created_on=models.DateTimeField(auto_now_add=True)


class Messages(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    message = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    message =models.ForeignKey(Messages, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
