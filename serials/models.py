from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200, default='American_dad')
    serie = models.IntegerField()
    episode = models.IntegerField()
    url1 = models.TextField()
    url1_cc = models.IntegerField(default=0)
    url2 = models.TextField(default='')
    url2_cc = models.IntegerField(default=0)
    url1_cz = models.TextField(default='')
    url2_cz = models.TextField(default='')
    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Serials(models.Model):
    name = models.CharField(max_length=200, default='American_dad')
    title = models.CharField(max_length=200)
    title_cz = models.TextField(default='')
    sub_title = models.TextField(default='')
    url1 = models.CharField(max_length=400)
    url2 = models.CharField(max_length=400)
    image = models.CharField(max_length=200)
    start_yr = models.IntegerField(default=0)
    end_yr = models.IntegerField(default=0)
    zaner = models.TextField(default='')
    delka = models.IntegerField(default=0)
    delka = models.IntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Topserials(models.Model):
    name = models.CharField(max_length=200, default='Brickleberry')
    image = models.CharField(max_length=200, default='brickleberry_small.jpg')

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


