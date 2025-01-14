from django.contrib import admin
from .models import User, Project, Task, TaskFile, ProjectMember, Comment, TaskHistory

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskFile)
admin.site.register(ProjectMember)
admin.site.register(Comment)
admin.site.register(TaskHistory)
