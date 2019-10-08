from django import forms
from .models import LoginUser
class LoginForm(forms.ModelForm):
	username = forms.CharField(label='Username')
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = LoginUser
		fields = [
			'username',
			'password',
		]