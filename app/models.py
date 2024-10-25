from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    pass


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default='')
    word_count = models.IntegerField()
    twitter_post = models.TextField(blank=True, default='')
    status = models.CharField(
        max_length=20,
        choices=(
            ("draft", "draft"),
            ("in_progress", "in progress"),
            ("published", "published")
        ),
        default="draft"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)