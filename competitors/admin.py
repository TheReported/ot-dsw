from django.contrib import admin

from .models import Competitor


@admin.register(Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'slug', 'job', 'avatar']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    raw_id_fields = ['music_styles']
