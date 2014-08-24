from django.contrib import admin
from .models import Artist
# Register your models here.
from .models import Artist
from tracks.models import Track

class TrackInLine(admin.StackedInline):
    model = Track
    extra = 1

from albums.models import Album

class AlbumInLine(admin.StackedInline):
    model = Album
    extra = 1

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    inlines = [TrackInLine, AlbumInLine]
    filter_horizontal = ('favorite_songs',)

admin.site.register(Artist, ArtistAdmin)