from rest_framework import serializers
from .models import Service, ServiceContent, ServiceCategory


# ServiceCategory Serializer
class ServiceCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceCategory
        read_only_fields = ('id',)
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        depth = 3
        read_only_fields = ('id',)
        fields= '__all__'

class ServiceContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceContent
        depth = 2
        read_only_fields = ('id',)
        fields= '__all__'


