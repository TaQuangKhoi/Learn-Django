from django.contrib import admin
from .models import Author, Messages

admin.site.register(Author)
admin.site.register(Messages)