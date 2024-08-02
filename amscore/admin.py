from django.contrib import admin
from .models import Anime, Reviews


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'started_airing')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'anime')