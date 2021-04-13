from rest_framework import serializers
from .models import SubCategory, Category, PostInfo, PostImage


# Category Serializer
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        read_only_fields = ('id',)
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        read_only_fields = ('id','category')
        fields = '__all__'

class PostInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostInfo
        depth = 2
        read_only_fields = ('id',)
        fields= '__all__'

class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        depth = 2
        read_only_fields = ('id',)
        fields= '__all__'


