from django.contrib import admin

from .models import Album, AudioFile, Broadcast, Playlist, Song, Uploadsong

# Register your models here.
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Broadcast)
admin.site.register(AudioFile)
admin.site.register(Playlist)
admin.site.register(Uploadsong)