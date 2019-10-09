from django.shortcuts import render
from Login.views import login_page
from django.http import HttpRequest 
from .forms import SignupForm
# Create your views here.
def signup_page(request):
	form = SignupForm(request.POST or None)
	context = {
		"form": form
	}
	if form.is_valid():
		form.save()
		return login_page(HttpRequest());
	else:
		return render(HttpRequest(),"Signup.html",context);