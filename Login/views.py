from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
def login_page(request,*args,**kwargs):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		form.save()
	context = {
		"form": form
	}
	return render(request,"Login.html",context)