from django.shortcuts import render
from django.http import JsonResponse
# from rest_framework.views import APIView
# from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import post
from rest_framework.decorators import api_view
from .serializers import postSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY)
            serializer = UserSerializer(user)
            data = {'user': serializer.data, 'token': auth_token}
            return Response(data, status=status.HTTP_200_OK)
            # SEND RES
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/post-list/',
        'Detail View':'/post-detail/<str:pk>/',
        'Create':'/post-create/',
        'Update':'/post-update/<str:pk>/',
        'Delete':'/post-delete/<str:pk>/',
    }
    return Response(api_urls)
@api_view(['GET'])
def postList(request):
    posts = post.objects.all()
    serializer = postSerializer(posts, many=True)
    return  Response(serializer.data)


@api_view(['GET'])
def postDetail(request, pk):
    posts = post.objects.get(id=pk)
    serializer = postSerializer(posts, many=False)
    return  Response(serializer.data)

@api_view(['POST'])
def postCreate(request):
    serializer = postSerializer(data=request.data)

    if serializer.is_valid():
       serializer.save 

    return  Response(serializer.data)

@api_view(['POST'])
def postUpdate(request, pk):
    posts = post.objects.get(id=pk)
    serializer = postSerializer(instance=post, data=request.data)

    if serializer.is_valid():
       serializer.save 

    return  Response(serializer.data)

@api_view(['DELETE']) 
def postDelete(request, pk):
    posts = post.objects.get(id=pk)
    posts.delete()

    return  Response('item successfully deleted')


# class postList(APIView):
#     def get(self, request):
#         post1 = post.objects.all()
#         serializer = postSerializer(post1, many=True)
#         return  Response(serializer.data)

#     def post(self):
#         pass

# class  PostListAPIView(ListAPIView):
#     queryset = post.pbjects.all()



# class  PostDetailAPIView(RetrieveAPIView):
#     def get(self, request):
#         post1 = post.objects.all()
#         serializer = postSerializer(post1, many=True)
#         return  Response(serializer.data)

#     queryset = post.objects.all()
#     serializer_class=postSerializer