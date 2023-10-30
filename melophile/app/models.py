from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist=models.CharField(max_length=50)
    genre=models.CharField(max_length=30,default='',blank=True, null=True)
    duration=models.DurationField()
    audio=models.FileField(upload_to='songs/')
    image=models.ImageField(upload_to='images/',blank=True, null=True)


    def __str__(self):
        return self.title
    

class Album(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    cover_art = models.ImageField(upload_to='albums/')
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.title
    

class Broadcast(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class AudioFile(models.Model):
    broadcast = models.ForeignKey(Broadcast, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='songs/')
    audio_name = models.CharField(max_length=300, default='')
    desc=models.CharField(max_length=1000, default='')
 

    def __str__(self):
        return self.audio_name
    
class Playlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    songs = models.ManyToManyField('Song', related_name='playlists', blank=True)


from django.db import models
from django.contrib.auth.models import User

class Uploadsong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,default='')
    audio_file = models.FileField(upload_to='songs/')
    image = models.ImageField(upload_to='images/', blank=True, null=True,default='')

    def __str__(self):
        return self.title

    
  