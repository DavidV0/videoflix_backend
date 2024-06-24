from django.contrib import admin
from .models import Movie
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class MovieResource(resources.ModelResource):
    class Meta:
        model = Movie

@admin.register(Movie)
class MovieAdmin(ImportExportModelAdmin):
    list_display = ['title', 'description', 'release_date']
    fields = ['title', 'description', 'release_date', 'thumbnail_file', 'video_file']
