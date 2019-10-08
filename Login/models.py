from django.db import models

# Create your models here.
class LoginUser(models.Model):
	username = models.TextField(max_length=15)
	password = models.TextField(max_length=30)