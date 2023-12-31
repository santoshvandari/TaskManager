from django.db import models

# Create your models here.
# Model To Store the Task Details 
class TaskInfo(models.Model):
    task_desc = models.TextField()
    task_status = models.BooleanField(default=False)
    task_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.task_name
    class Meta:
        db_table = 'TaskInfo'
        verbose_name_plural = 'TaskInfo'
        ordering = ['-task_created']