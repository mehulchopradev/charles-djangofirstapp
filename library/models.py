from django.db import models
from datetime import date

class Publication(models.Model):
    name = models.CharField(max_length=50, null=False)
    ratings = models.IntegerField(null=True)
    # book_set

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100, null=False)
    price = models.FloatField(null=False)
    pages = models.IntegerField(null=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, default=None)
    count = models.IntegerField(null=False, default=0)
    published_date = models.DateField(null=False, default=date.today())
    # review_set
    # student_set

    def __str__(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=500, null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=40, null=False, unique=True)
    password = models.CharField(max_length=10, null=False)
    country = models.CharField(max_length=3, null=False)

    books_issued = models.ManyToManyField(Book)
