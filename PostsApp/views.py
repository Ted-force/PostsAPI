from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from PostsApp.models import Post, Comments, Like
from PostsApp.serializers import PostSerializer, CommentSerializer, LikeSerializer

# Create your views here.

@csrf_exempt
def post_list(request, id=0):
    if request.method == 'GET' and id == 0:
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'GET' and id != 0:
        posts = Post.objects.filter(postID=id)
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        postData = JSONParser().parse(request)
        post = Post.objects.get(postID=postData['postID'])
        serializer = PostSerializer(post, data=postData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        post = Post.objects.get(postID=id)
        post.delete()
        return JsonResponse({'deleted': True})
        
@csrf_exempt
def comment_list(request, id=0):
    if request.method == 'GET' and id != 0:
        comments = Comments.objects.filter(post_id=id)
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        commentData = JSONParser().parse(request)
        comment = Comments.objects.get(commentID=commentData['commentID'])
        # comment = Comments.objects.get(commentID=commentData['id'])
        serializer = CommentSerializer(comment, data=commentData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        comment = Comments.objects.get(id=id)
        comment.delete()
        return JsonResponse({'deleted': True}) 

@csrf_exempt
def like_list(request, id=0):
    if request.method == 'GET' and id != 0:
        likes = Like.objects.filter(post_id=id)
        serializer = LikeSerializer(likes, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LikeSerializer(data=data)
        print(data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'PUT':
        likeData = JSONParser().parse(request)
        like = Like.objects.get(id=likeData['id'])
        serializer = LikeSerializer(like, data=likeData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        like = Like.objects.get(id=id)
        like.delete()
        return JsonResponse({'deleted': True})                       

