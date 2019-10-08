from django.db import models

# Create your models here.
class User(models.Model):
	username = models.TextField(max_length=15)
	password = models.TextField(max_length=30)
	name = models.TextField(max_length=100)