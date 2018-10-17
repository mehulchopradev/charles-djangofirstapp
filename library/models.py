from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=40, null=False, unique=True)
    password = models.CharField(max_length=10, null=False)
    country = models.CharField(max_length=3, null=False)

class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False)
    pages = models.IntegerField(null=True)

    def __str__(self):
        return self.title
