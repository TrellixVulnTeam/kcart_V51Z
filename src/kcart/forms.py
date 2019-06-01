from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class contact_form(forms.Form):
	fullname = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"your fullname"}))	
	email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email address"}))
	message = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"message"}))

class login_form(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

class register_form(forms.Form):
	username = forms.CharField()
	email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email address"}))
	password = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(label = "confirm password" , widget=forms.PasswordInput())

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("password must match !")
		return data 
	def clean_username(self):
		data = self.cleaned_data
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username already exists !")
		return username
	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email already exists !")
		return email