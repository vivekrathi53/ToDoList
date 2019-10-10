from django.shortcuts import render
from .forms import LoginForm
from .models import LoginUser
from Signup.models import SignupUser
from django.http import HttpRequest
# Create your views here.
def login_page(request,*args,**kwargs):
	#try:
	#	print(request.META.get('HTTP_REFERER'))
	#except:
	#	print("NO REFERER")
	form = LoginForm(request.POST or None)
	if form.is_valid():
		return authenticate_page(request)
	context = {
		"form": form
	}
	return render(request,"Login.html",context)
def authenticate_page(request,*args,**kwargs):
	us = request.POST.get("username")
	pas = request.POST.get("password")
	try:
		obj = SignupUser.objects.get(username=us)
	except:
		return login_page(HttpRequest())
	if pas == obj.password:
		return render(request,"Home.html",{})
	else:
		return login_page(HttpRequest())
