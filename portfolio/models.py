from django.db import models

# Create your models here.
from natives.models import Native


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.TextField(default="https://thumbs.dreamstime.com/b/project-management-concept-27391266.jpg")
    date_created = models.DateTimeField(auto_now_add=True)
    native = models.ForeignKey(Native, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
