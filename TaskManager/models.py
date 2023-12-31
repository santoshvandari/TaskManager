from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model To Store the Task Details 
class TaskInfo(models.Model):
    # linking the task table with username of the user 
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    task_desc = models.TextField()
    task_status = models.BooleanField(default=False)
    task_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'TaskInfo'
        verbose_name_plural = 'TaskInfo'
        ordering = ['-task_created']