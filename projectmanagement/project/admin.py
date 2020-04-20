from django.contrib import admin
from projectmanagement.project.models import User, Project, Income
# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Income)