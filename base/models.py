from django.db import models
from django.utils.text import slugify

# Create your models here.

class Videos(models.Model):
    media_name = models.CharField(max_length=150)
    video = models.FileField(upload_to='media',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.media_name)
    

class VideoSegment(models.Model):
    video = models.ForeignKey(Videos,on_delete=models.CASCADE)
    segment_name = models.CharField(max_length=150,null=True,blank=True)
    video_segment = models.FileField(upload_to='media/segment',null=True,blank=True)

    def __str__(self):
        return str(self.segment_name)