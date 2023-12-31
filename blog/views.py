from django.shortcuts import render
from blog.models import *
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response




class RegisterView(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=RegisterSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                'data' : serializer.errors,
                'message': 'something went wrong'

                }, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({
                'data' : {},
                'message': ' account is created'

            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            print(e)
            return Response({
                'data' : {},
                'message': 'something went wrong'

            }, status=status.HTTP_400_BAD_REQUEST)
                
class BlogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100 


class BlogView(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    permission_classes=[IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'blog_text']
    pagination_class = BlogPagination
    


class Tagview(viewsets.ModelViewSet):
    queryset=Tags.objects.all()
    serializer_class = TagSerializer
    permission_classes=[IsAuthenticated]


class Commentview(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes=[IsAuthenticated]



class PublicView(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'blog_text']
    pagination_class = BlogPagination
    permission_classes = [AllowAny]


class likeView(viewsets.ModelViewSet):
    queryset=Likes.objects.all()
    serializer_class = LikesSerializer
    permission_classes=[IsAuthenticated]
    
  