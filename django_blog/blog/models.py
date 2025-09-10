from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone  # Needed for default
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)  # Add this field
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # TaggableManager for tags
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# New Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})