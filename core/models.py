from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    thumbnail_file = models.ImageField(upload_to='thumbnails', blank=True, null=True)
    video_file = models.FileField(upload_to='videos', blank=True, null=True)
    video_480p = models.CharField(max_length=255, blank=True, null=True)
    video_720p = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
