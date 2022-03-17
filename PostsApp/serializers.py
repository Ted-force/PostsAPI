from rest_framework import serializers
from PostsApp.models import Post, Comments, Reactions

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('postID', 'title', 'body', 'username', 'created_at', 'reactionsCount', 'commentscount')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','post', 'username', 'comment', 'comment_date')

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reactions
        fields = ('id','user', 'post', 'reactionType')
                