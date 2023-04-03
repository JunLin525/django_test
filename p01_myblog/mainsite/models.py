from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug =models.CharField(max_length=200)
    abstract = models.CharField(max_length=200)
    pic_url = models.URLField(max_length=250)
    body =models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return str(self.title)