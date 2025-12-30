from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # Title of the post
    title = models.CharField(max_length=200)
    # Main content of the post
    content = models.TextField()
    # Date published - automatically set when created
    published_date = models.DateTimeField(auto_now_add=True)
    # Author linked to Django's built-in User model
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
