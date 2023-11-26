from django.contrib import admin

from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'slug', 'subject', 'avatar']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
