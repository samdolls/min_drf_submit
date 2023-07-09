from django.db import models

# Create your models here.
def image_upload_path(instance, filename):
    return f'{instance.id}/{filename}'

class Tag(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)

class Album(models.Model):
    id = models.AutoField(primary_key = True)
    artist = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    release = models.IntegerField()
    description = models.TextField(max_length = 200)
    tag = models.ManyToManyField(Tag, blank = True)

class AlbumImage(models.Model):
    id = models.AutoField(primary_key = True)
    album = models.ForeignKey(Album, on_delete = models.CASCADE, related_name = 'image')
    image = models.ImageField(upload_to = image_upload_path, blank = True, null = True)

class Track(models.Model):
    id = models.AutoField(primary_key = True)
    album = models.ForeignKey(Album, blank = False, null = False, on_delete = models.CASCADE, related_name = "tracks")
    number = models.IntegerField()
    title = models.CharField(max_length = 50)