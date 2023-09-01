from django.contrib import admin
from .models import Author, Messages


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "bio",)


class MessagesAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "message",)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Messages, MessagesAdmin)