from django.http import HttpResponse
from django.shortcuts import render , redirect
from .forms import contact_form , login_form , register_form
from django.contrib.auth import authenticate, login , get_user_model

def home_page(request):
	context= {
		"title":"its home page "
	}
	return render(request,"index.html",context)

def login_page(request):
	form = login_form(request.POST or None)
	context= {
		"title":"Login",
		"form": login_form
	}
	print(request.user.is_authenticated())
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			return redirect("/login")
		else:
			print("error")
	return render(request,"auth/login.html",context)

user = get_user_model()
def register_page(request):
	form = register_form(request.POST or None	)
	context= {
		"title":"Register",
		"form": register_form
	}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		email = form.cleaned_data.get("email")
		new_user = user.objects.create_user(username,email,password)
		print(new_user)
	return render(request,"auth/register.html",context)

def about_page(request):
	return render(request,"index.html",{})

def contact_page(request):
	contact_forms = contact_form(request.POST or None)
	context= {
		"title":"Contact Us: ",
		"content":"Contact Form",
		"form": contact_forms
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
	return render(request,"contact/contact.html",context)