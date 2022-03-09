# from django.conf.urls import url
from django.urls import path
from PostsApp.views import *
from PostsApp.views2 import PostList, CommentList, LikeList

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:id>',PostList.as_view()),
    path('posts/<int:id>/comments/',CommentList.as_view()),
    path('posts/<int:id>/comments/<int:id2>',CommentList.as_view()),
    path('posts/<int:id>/likes/',LikeList.as_view()),
    path('posts/<int:id>/likes/<int:id2>',LikeList.as_view()),
]


# eg: http://127.0.0.1:8000/api/posts/
    #   http://127.0.0.1:8000/api/posts/1
    #    http://127.0.0.1:8000/api/posts/1/comments/
    #    http://127.0.0.1:8000/api/posts/1/comments/1
