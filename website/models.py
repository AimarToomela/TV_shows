from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TVShow(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="No description available")
    image_url = models.URLField(default="https://via.placeholder.com/300?text=No+Image+Available")
    featured = models.BooleanField(default=False)
    favorite_user = models.ManyToManyField(User, related_name='favorites', blank=True)

    def __str__(self):
        return self.title
