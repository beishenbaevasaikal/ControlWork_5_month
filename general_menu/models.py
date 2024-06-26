from django.db import models

class Slogan(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class VideoYouTube(models.Model):
    video = models.URLField()

    def __str__(self):
        return self.video

class TopProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=80)
    photo = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name