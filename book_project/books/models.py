from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


