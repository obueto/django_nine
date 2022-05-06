from django.db import models


# Create your models here.
class Cohort(models.Model):
    number = models.IntegerField(default=0, unique=True)
    name = models.CharField(max_length=50, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.name


GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'others')
)


class Native(models.Model):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='others')
    number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE)


def __str__(self) -> str:
    return self.first_name + " " + self.last_name
