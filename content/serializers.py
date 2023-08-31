from rest_framework import serializers
from . models import Category, Content



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

   


class ContentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Content
        fields = "__all__"

    
    # def create(self, validated_data):
    #     category_names = validated_data.pop('categories').split(',')
    #     categories = []

    #     for category_name in category_names:
    #         category, created = Category.objects.get_or_create(name=category_name)
    #         categories.append(category.id)

    #     # validated_data['categories'] = categories
    #     content = Content.objects.create(**validated_data)
    #     content.categories.set(categories)

    #     return content



    


    
