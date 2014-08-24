from django.contrib import admin

# Register your models here.
from actions import export_as_csv
from .models import Track

class TrackAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'order', 'album', 'player', 'es_pharrel')
    list_filter = ('artist', 'album')

    search_fields = ('title', 'artist__first_name')

    list_editable = ('title','album')

    actions = (export_as_csv,)

    raw_id_fields = ('artist',)

    def es_pharrel(self, obj):
        return obj.id == 1

    es_pharrel.boolean = True

admin.site.register(Track, TrackAdmin)