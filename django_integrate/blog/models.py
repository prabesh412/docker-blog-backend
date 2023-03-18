from datetime import datetime

from django.db import models
from django.utils.text import slugify
from django.conf import settings



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogPost(BaseModel):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, primary_key=True)
    category = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
