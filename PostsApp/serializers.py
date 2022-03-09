from rest_framework import serializers
from PostsApp.models import Post, Comments, Like

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('postID', 'title', 'body', 'username', 'created_at', 'likescount', 'commentscount')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','post', 'username', 'comment', 'comment_date')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id','user', 'post')
                