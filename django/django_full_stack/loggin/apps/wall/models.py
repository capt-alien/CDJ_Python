from django.db import models
from apps.loggin_app.models import Users

# Create your models here.
class Messages(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    message = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    message_id =models.ForeignKey(Messages, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
