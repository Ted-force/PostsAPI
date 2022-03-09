from datetime import timezone
from django.db import models

# Create your models here.
class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    username = models.CharField(max_length=200)
    likescount = models.IntegerField(default=0)
    commentscount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)    
    username = models.CharField(max_length=200)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.CharField(max_length=200)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
