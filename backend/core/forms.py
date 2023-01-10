from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Contact, Project, Comment, Gallery

class SignUpForm(UserCreationForm):
	# first_name = forms.CharField(max_length=50, required=True)
	# last_name = forms.CharField(max_length=50, required=True)
	email = forms.EmailField(max_length=255, required=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2',]
		# exclude = ['first_name','last_name']

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['email', 'message']
		def __init__(self):
			self.fields['email'].label = ''

class NewProj(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['thumbnail', 'title', 'description', 'frontpage', 'frontpageText', 'featureSignIn', 'featureSignInText', 'featureCrud', 'featureCrudText','featureDashboard', 'featureDashboardText', 'responsive1', 'responsive2', 'responsive3', 'url']

class GalleryForm(forms.ModelForm):
	class Meta:
		model = Gallery
		fields = ['name', 'image', 'video']