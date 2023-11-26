from django.contrib import admin

from .models import MusicStyle


@admin.register(MusicStyle)
class JudgeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
