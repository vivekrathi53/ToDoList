from django.shortcuts import render

# Create your views here.
def login_page(request,*args,**kwargs):
	return render(request,"Login.html",{})