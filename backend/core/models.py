from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
	title = models.CharField(max_length=100, unique=True, blank=True,null=True)
	slug = models.SlugField(max_length=100, unique=True, blank=True,null=True)
	description = models.TextField(max_length=255, blank=True,null=True)

	frontpage = models.ImageField(upload_to='uploads/', blank=True, null=True)
	frontpageText = models.TextField(max_length=255,blank=True, null=True)

	featureSignIn = models.ImageField(upload_to='uploads/', blank=True, null=True)
	featureSignInText = models.TextField(max_length=255, blank=True,null=True)

	featureDashboard = models.ImageField(upload_to='uploads/', blank=True, null=True)
	featureDashboardText = models.TextField(max_length=255, blank=True,null=True)

	featureCrud = models.ImageField(upload_to='uploads/', blank=True, null=True)
	featureCrudText = models.TextField(max_length=255, blank=True,null=True)

	responsive1 = models.ImageField(upload_to='uploads/', blank=True, null=True)
	responsive2 = models.ImageField(upload_to='uploads/', blank=True, null=True)
	responsive3 = models.ImageField(upload_to='uploads/', blank=True, null=True)

	url = models.URLField(blank=True,null=True)
	upvotes = models.IntegerField(default=0)

	def __str__(self):
		return self.title

class Contact(models.Model):
	email = models.EmailField(max_length=255, unique=True)
	message = models.TextField(max_length=255)

	def __str__(self):
		return self.email

class Comment(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
	on = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
	message = models.TextField(max_length=255)
	timestamp = models.DateTimeField(auto_now_add=True)
	upvotes = models.IntegerField(default=0)
	active = models.BooleanField(default=False)

	def __str__(self):
		return f'Comment by {self.username} on {self.on}'

class Gallery(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='uploads/gallery/', blank=True, null=True)
	video = models.FileField(upload_to='uploads/gallery/video/', blank=True, null=True)
	upvotes = models.IntegerField(default=0)
	def __str__(self):
		return self.name