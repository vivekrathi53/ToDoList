from django import forms
from .models import User
class LoginForm(forms.ModelForm):
	username = forms.CharField(label='Username')
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'name',
		]