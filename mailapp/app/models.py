from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.name


class Messages(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
