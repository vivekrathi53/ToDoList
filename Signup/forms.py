from .models import SignupUser
from django import forms
class SignupForm(forms.ModelForm):
	username = forms.CharField(label='Username')
	password = forms.CharField(widget=forms.PasswordInput)
	name = forms.CharField(label='Name')
	date_of_birth = forms.DateField(input_formats=['%d/%m/%Y']);
	class Meta:
		model = SignupUser
		fields = [
			'username',
			'password',
			'name',
			'email',
			'date_of_birth',
		]