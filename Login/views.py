from django.shortcuts import render
from .forms import LoginForm
from .models import User
# Create your views here.
def login_page(request,*args,**kwargs):
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
	obj = User.objects.get(username=us)
	if pas == obj.password:
		return render(request,"Home.html",{})
	else:
		return render(request,"Login.html",{})
	

