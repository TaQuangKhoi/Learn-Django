from django.contrib import admin
from .models import Category, Course, Lesson, Tag
from django.utils.html import format_html


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'description', 'image', 'active', 'created_date', 'updated_date', 'category']
    search_fields = ['subject', 'created_date', 'category__name']
    readonly_fields = ['feature_image']

    def feature_image(self, course):
        return format_html(
            '<img src="/static/{0}" width="240 px"/>',
            course.image.name
        )


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'content', 'image', 'active', 'created_date', 'updated_date', 'course']
    search_fields = ['subject', 'created_date', 'course__subject']

    readonly_fields = ['feature_image']

    def feature_image(self, course):
        return format_html(
            '<img src="/static/{0}" width="240 px"/>',
            course.image.name
        )


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
