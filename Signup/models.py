from django.db import models

# Create your models here.
class SignupUser(models.Model):
	username = models.TextField(max_length=15)
	password = models.TextField(max_length=30)
	name = models.TextField(max_length=30)
	date_of_birth = models.DateField()
	email = models.EmailField()
	