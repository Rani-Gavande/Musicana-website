from django.db import models

# Create your models here.
class SignUp(models.Model):
    id=models.IntegerField(primary_key=True)
    Username=models.CharField(max_length=255 ,null=True,blank=True,unique=True)
    password=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(max_length=100 , null=True,blank=True)
    phone=models.CharField(max_length=15 , null=True,blank=True,unique=True)
    profile=models.ImageField(upload_to='profiles',null=True,blank=True)
    def __str__(self):
        return self.Username

class Artist(models.Model):
    id=models.IntegerField(primary_key=True)
    Artist_name = models.CharField(max_length=255)
    Artist_Image=models.URLField(max_length=255)
    Listener=models.CharField(max_length=255 ,blank=True,null=True)
    def __str__(self):
        return self.Artist_name 

class Album(models.Model):
    id=models.IntegerField(primary_key=True)
    Album_name = models.CharField(max_length=255)
    Album_Image=models.URLField(max_length=255)
    Listener=models.CharField(max_length=255 ,blank=True,null=True)
    def __str__(self):
        return self.Album_name


class TRENDINGSong(models.Model):
    Song_Id=models.IntegerField(primary_key=True)
    Song_name=models.CharField(max_length=255)
    Artist_name=models.CharField(max_length=255)
    Song_Image=models.URLField(max_length=255)
    Song_Audio=models.FileField(upload_to='TrendingSong')
    def __str__(self):
        return self.Song_name 
    
class PopularSong(models.Model):
    Song_Id=models.IntegerField(primary_key=True)
    Song_name=models.CharField(max_length=255)
    Artist_name=models.CharField(max_length=255)
    Song_Image=models.URLField(max_length=255)
    Song_Audio=models.FileField(upload_to='PopularSong')
    def __str__(self):
        return self.Song_name 
    
class ArtistSong(models.Model):
    Song_Id=models.IntegerField()
    Song_name = models.CharField(max_length=255)
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    Song_Audio = models.FileField(upload_to='ArtistSong')
    Song_Image=models.URLField(max_length=255)
    def __str__(self):
        return self.Song_name


class AlbumSong(models.Model):
    Song_Id=models.IntegerField()
    Song_name = models.CharField(max_length=255)
    Album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    Song_Audio = models.FileField(upload_to='AlbumSong')
    Song_Image=models.URLField(max_length=255)
    def __str__(self):
        return self.Song_name
    
class MarathiSong(models.Model):
    Song_Id=models.IntegerField(primary_key=True)
    Song_name=models.CharField(max_length=255)
    Artist_name=models.CharField(max_length=255)
    Song_Image=models.URLField(max_length=255)
    Song_Audio=models.FileField(upload_to='MarathiSong')
    def __str__(self):
        return self.Song_name 
class TamilSong(models.Model):
    Song_Id=models.IntegerField(primary_key=True)
    Song_name=models.CharField(max_length=255)
    Artist_name=models.CharField(max_length=255)
    Song_Image=models.URLField(max_length=255)
    Song_Audio=models.FileField(upload_to='TamilSong')
    def __str__(self):
        return self.Song_name 
    