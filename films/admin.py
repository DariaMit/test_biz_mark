from django.contrib import admin
from.models import Film, Genre, Gallery


class GalleryInline(admin.TabularInline):
    fk_name = 'film'
    model = Gallery


class FilmsAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
    list_display = ('id', 'title', 'slug', 'production_date', 'actors', 'director')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title','production_date', 'actors', 'director')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'slug')


admin.site.register(Film, FilmsAdmin)
admin.site.register(Genre, GenreAdmin)