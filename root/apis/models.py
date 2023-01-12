from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(BaseModel):
    title = models.CharField(max_length=80)
    description = models.TextField()
    complete = models.BooleanField()

    class Meta:
        ordering = ['-created']
        db_table = 'task'

    def __str__(self):
        return self.title
