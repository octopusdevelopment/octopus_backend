from django.shortcuts import  get_object_or_404, render
from django.http import HttpResponse, Http404

# REST FRAMEWORK
from rest_framework import status
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.reverse import reverse


# MODELS
from .models import PostImage, PostInfo, Category, SubCategory

# SERIALIZERS
from .serializers import PostImageSerializer, PostInfoSerializer, \
                         CategorySerializer, SubCategorySerializer

# PAGINATION
from rest_framework.pagination import PageNumberPagination

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1

class PostInfoCreateAPIView(generics.ListCreateAPIView):
    queryset = PostInfo.postobjects.all()
    serializer_class = PostInfoSerializer
    permission_classes = (IsAuthenticated, )


class PostListAPIView(generics.ListAPIView):
    
    queryset = PostInfo.postobjects.all()
    serializer_class = PostInfoSerializer

    permission_classes = (AllowAny, )
    pagination_class = StandardResultsSetPagination


class PostDetailAPIView(generics.RetrieveAPIView):

    serializer_class = PostImageSerializer
    permission_classes = (AllowAny, )
    
    def get_object(self):
        obj = get_object_or_404(PostImage, post__show=True, post__slug=self.kwargs["slug"])
        return obj


class PostInfoAPIView(generics.RetrieveAPIView):

    serializer_class = PostInfoSerializer
    permission_classes = (AllowAny, )
    
    def get_object(self):
        obj = get_object_or_404(PostInfo, show=True, slug=self.kwargs["slug"])
        return obj


class CategoryAPIView(generics.RetrieveAPIView):

    serializer_class = CategorySerializer
    permission_classes = (AllowAny, )
    
    def get_object(self):
        obj = get_object_or_404(Category, id=self.kwargs["id"])
        return obj

class SubCategoryAPIView(generics.RetrieveAPIView):

    serializer_class = SubCategorySerializer
    permission_classes = (AllowAny, )
    
    def get_object(self):
        obj = get_object_or_404(SubCategory, id=self.kwargs["id"])
        return obj