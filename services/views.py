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
from .models import Service, ServiceContent, ServiceCategory

# SERIALIZERS
from .serializers import ServiceContentSerializer, ServiceSerializer, \
                        ServiceCategorySerializer

# PAGINATION
from rest_framework.pagination import PageNumberPagination

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 12


# Show service categories

class ServiceCategoryListAPIView(generics.ListAPIView):

    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer

    permission_classes = (AllowAny, )
    pagination_class = StandardResultsSetPagination


# Show services that are in a particular category

class ServiceListOfCategoryAPIView(generics.ListAPIView):

    serializer_class = ServiceSerializer

    permission_classes = (AllowAny, )
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Service.serviceobjects.filter(category__slug=self.kwargs["slug"])
        return queryset


# Show the content of a particular service

class ServiceContentAPIView(generics.ListAPIView):

    serializer_class = ServiceContentSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        queryset = ServiceContent.objects.filter(service__show=True, service__slug=self.kwargs["slug"])
        return queryset


# Show services that should appear in home

class ServiceHomeAPIView(generics.ListAPIView):

    serializer_class = ServiceSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        queryset = Service.serviceobjects.filter(show_home=True)
        return queryset
