from django.urls import path
from .views import ServiceListOfCategoryAPIView, ServiceContentAPIView, \
     ServiceCategoryListAPIView, ServiceHomeAPIView

urlpatterns = [
    path('', ServiceCategoryListAPIView.as_view(), name='services-all-categories'),
    path('home', ServiceHomeAPIView.as_view(), name='service-in-home'),
    path('<slug:slug>', ServiceListOfCategoryAPIView.as_view(), name='services-per-category'),
    path('content/<slug:slug>', ServiceContentAPIView.as_view(), name='service-content'),
   
]