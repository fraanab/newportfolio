from django.urls import path, include
from .views import frontpage, project, signup, dashboard, upvoteProj, upvoteComm, deletecomment, deleteproj, deletemail, deletePic, gallery, newpic, upvotePic
from django.contrib.auth import views
from django.contrib import admin

urlpatterns = [
	path('', frontpage, name="frontpage"),
	path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('dashboard/', dashboard, name="dashboard"),
	path('upvoteproj/<slug:slug>/', upvoteProj, name='upvoteProj'),
	path('upvotecomm/<int:pk>/', upvoteComm, name='upvoteComm'),
	path('deletecomm/<int:pk>/', deletecomment, name='deletecomment'),
	path('deleteproj/<slug:slug>/', deleteproj, name='deleteproj'),
	path('deletemail/<int:pk>/', deletemail, name='deletemail'),
	path('gallery/', gallery, name='gallery'),
	path('upvotepic/<str:name>/', upvotePic, name='upvotepic'),
	path('deletepic/<str:name>/', deletePic, name='deletepic'),
	path('newpic/', newpic, name='newpic'),
	path('project/<slug:slug>/', project, name="project"),
]