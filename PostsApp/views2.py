from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView


from PostsApp.models import Post, Comments, Reactions
from PostsApp.serializers import PostSerializer, CommentSerializer, ReactionSerializer

# Create your views here.

class PostList(APIView):
    def get(self, request, id=0):
        if id == 0:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            posts = Post.objects.filter(postID=id)
            serializer = PostSerializer(posts, many=True)
            return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def put(self, request, id):
        postData = JSONParser().parse(request)
        post = Post.objects.get(postID=id)
        serializer = PostSerializer(post, data=postData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id):
        post = Post.objects.get(postID=id)
        post.delete()
        return JsonResponse({'deleted': True})

class CommentList(APIView):
    def get(self, request, id=0,id2=0):
        if id != 0:
            if id2 != 0:
                comments = Comments.objects.filter(id=id2)
                serializer = CommentSerializer(comments, many=True)
                return JsonResponse(serializer.data, safe=False)
            comments = Comments.objects.filter(post_id=id)
            serializer = CommentSerializer(comments, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'No post id'}, status=400)

    def post(self, request, id=0):
        if id != 0:
         posts = Post.objects.get(postID=id)
         posts.commentscount += 1
         posts.save()

         data = JSONParser().parse(request)
         data['post'] = id
         serializer = CommentSerializer(data=data)
         if serializer.is_valid():            
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def put(self, request,id, id2):
        posts = Post.objects.get(postID=id)
        commentData = JSONParser().parse(request)
        commentData['post'] = id
        comment = Comments.objects.get(id=id2)
        serializer = CommentSerializer(comment, data=commentData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, id,id2):
        comment = Comments.objects.get(id=id2)
        comment.delete()
        return JsonResponse({'deleted': True})         




class ReactionList(APIView):
    def get(self, request, id=0):
        if id != 0:
            reactions = Reactions.objects.filter(post_id=id)
            serializer = ReactionSerializer(reactions, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'No post id'}, status=400)

    def post(self, request, id=0, id2=0):
        if id != 0:
            posts = Post.objects.get(postID=id)
            posts.reactionsCount += 1
            posts.save()
            data = JSONParser().parse(request)
            data['post'] = id
            if(id2 == 0):
                data['reactionType'] = 'like'
            elif(id2 == 1):
                data['reactionType'] = 'Laugh'
            elif(id2 == 2):
                data['reactionType'] = 'Amazed'
            elif(id2 == 3):
                data['reactionType'] = 'Sad'            
            serializer = ReactionSerializer(data=data)
            if serializer.is_valid():
               serializer.save()
               return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        
    def delete(self, request, id,id2,id3):
        reaction = Reactions.objects.get(id=id3)
        reaction.delete()
        return JsonResponse({'deleted': True})


       


