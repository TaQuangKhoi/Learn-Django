from django.contrib import admin

from members.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)


# Register your models here.
admin.site.register(Member, MemberAdmin)
