from django.contrib import admin
from TaskManager.models import TaskInfo

# Register your models here.
class TaskInfoDispaly(admin.ModelAdmin):
    list_display = ['user','task_desc','task_status','task_created']
    list_filter = ['user','task_status']
    search_fields = ['user','task_desc','task_status','task_created']

# Register the TaskInfo Model
admin.site.register(TaskInfo,TaskInfoDispaly)
