from django.contrib import admin
from .models import Project, Contact, Comment, Gallery

admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Comment)
admin.site.register(Gallery)