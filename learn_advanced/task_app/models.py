from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/avatars/%Y/%m')


class Category(models.Model):
    # id - primary - auto increment
    name = models.CharField(max_length=200, null=False, unique=True)


class Course(models.Model):
    subject = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/courses/%Y/%m', default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.SET_NULL, null=True)


class Lesson(models.Model):
    subject = models.CharField(max_length=200, null=False)
    content = models.TextField()
    image = models.ImageField(upload_to='uploads/lessons/%Y/%m', default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='lessons', null=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
