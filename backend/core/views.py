from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Comment, Contact, Gallery
from django.contrib.auth import login
from .forms import SignUpForm, GalleryForm
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, NewProj
from django.http import HttpResponseRedirect

def frontpage(request):
	projects = Project.objects.all().order_by("-id")
	totalproj = projects.count()
	if request.method == 'POST':
		contactform = ContactForm(request.POST)
		if contactform.is_valid():
			contactform.save()
			return redirect('/')
	else:
		contactform = ContactForm()

	context = {
		'projects':projects,
		'totalproj':totalproj,
		'contactform': contactform
	}

	return render(request, 'frontpage.html', context)

def project(request, slug):
	project = get_object_or_404(Project, slug=slug)
	comments = project.comments.filter(active=True)
	if request.user.is_authenticated:
		if request.method == 'POST':
			username = request.user
			message = request.POST.get('message')
			Comment.objects.create(username=username, on=project, active=True, message=message)
			return redirect(f'/project/{slug}')
	return render(request, 'project.html', {'project':project, 'comments':comments})

def upvoteComm(request, pk):
	comment = Comment.objects.get(pk=pk)
	comment_upvotes = comment.upvotes + 1
	Comment.objects.filter(pk=pk).update(upvotes=comment_upvotes)
	return redirect('/')


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form':form})

def dashboard(request):
	if request.user.is_superuser:
		mails = Contact.objects.all()
		if request.method == 'POST':
			form = NewProj(request.POST, request.FILES)
			if form.is_valid():
				newform = form.save(commit=False)
				newform.slug = newform.title.replace(' ', '-')
				newform.thumbnail = request.FILES.get('thumbnail')
				newform.frontpage = request.FILES.get('frontpage')
				newform.featureSignIn = request.FILES.get('featureSignIn')
				newform.featureDashboard = request.FILES.get('featureDashboard')
				newform.featureCrud = request.FILES.get('featureCrud')
				newform.responsive1 = request.FILES.get('responsive1')
				newform.responsive2 = request.FILES.get('responsive2')
				newform.responsive3 = request.FILES.get('responsive3')
				newform.save()
				return redirect('/')
		else:
			form = NewProj()
		return render(request, 'dashboard.html', {'form':form, 'mails':mails})
	else:
		return redirect('/')

def upvoteProj(request, slug):
	project = get_object_or_404(Project, slug=slug)
	if request.user.is_authenticated:
		if request.method == 'POST':
			project.upvotes += 1
			Project.objects.filter(slug=slug).update(upvotes=project.upvotes)
			return redirect(f'/project/{slug}')
	else:
		return redirect('login')

def upvotePic(request, name):
	picture = Gallery.objects.get(name=name)
	picture_upvotes = picture.upvotes + 1
	Gallery.objects.filter(name=name).update(upvotes=picture_upvotes)
	return redirect('gallery')

@login_required
def deletePic(request, name):
	if request.user.is_superuser:
		if request.method == 'POST':
			picture = Gallery.objects.get(name=name)
			picture.delete()
			return redirect('gallery')
	else:
		return redirect('/')

@login_required
def deletecomment(request, pk):
	if request.method == 'POST':
		Comment.objects.filter(pk=pk).delete()
		return redirect('/')

@login_required
def deleteproj(request, slug):
	if request.user.is_superuser:
		if request.method == 'POST':
			proj = Project.objects.filter(slug=slug)
			proj.delete()
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

@login_required
def deletemail(request, pk):
	if request.method == 'POST':
		Contact.objects.filter(pk=pk).delete()
		return redirect('dashboard')

def gallery(request):
	pictures = Gallery.objects.all()
	form = GalleryForm()
	return render(request, 'gallery.html', {'pictures':pictures, 'form':form})
@login_required
def newpic(request):
	if request.user.is_superuser:
		if request.method == 'POST':
			form = GalleryForm(request.POST, request.FILES)
			if form.is_valid():
				newform = form.save(commit=False)
				newform.image = request.FILES.get('image')
				newform.video = request.FILES.get('video')
				newform.save()
				return redirect('gallery')
	else:
		return redirect('/')