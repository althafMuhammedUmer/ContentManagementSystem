from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from . serializers import CategorySerializer, ContentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . models import Content, Category
from rest_framework import status

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_content(request):
    
    category_names = request.data['categories'].split(',')
    categories = []

    for category_name in category_names:
        category, created = Category.objects.get_or_create(name=category_name)
        categories.append(category)
        
    
    content_data = {
        "author": request.user.id,
        "title": request.data.get('title'),
        "body": request.data.get('body'),
        "summary": request.data.get('summary'),
        "document" : request.data.get('document')
    }
    
    content_serializer = ContentSerializer(data=content_data)
    if content_serializer.is_valid():
        content = content_serializer.save()
        content.categories.set(categories)
        return Response(content_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(content_serializer.errors, status=400)

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_content(request, id=None):

    if id is None:
        content = Content.objects.all()
        serializer = ContentSerializer(content, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        try:
            content = Content.objects.get(id=id)
            serializer = ContentSerializer(content, many=False)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Content.DoesNotExist:
            return Response({"error": "Content does not exist"}, status=status.HTTP_404_NOT_FOUND)
        

    


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def content_actions(request, id=None):
    data = request.data.copy()
    data['author'] = request.user.id
    
    try:
        content = Content.objects.get(id=id)
    except Content.DoesNotExist:
        return Response({"error": "Content not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if 'categories' in data and data['categories'] is not None:
    
        category_names = request.data['categories'].split(',')
        categories = []

        for category_name in category_names:
            category, created = Category.objects.get_or_create(name=category_name)
            categories.append(category)
    
    content_data = {
        "author": request.user.id,
        "title": request.data.get('title'),
        "body": request.data.get('body'),
        "summary": request.data.get('summary'),
        "document": request.data.get('document', content.document)
        
    }

  
    if request.user == content.author:
        if request.method == "PUT":
            serializer = ContentSerializer(content, data=content_data)
            if serializer.is_valid():
                content = serializer.save()
                if 'categories' in data and data['categories'] is not None:
                    content.categories.clear() # clearing old data for storing updated data
                    content.categories.add(*categories)

                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == "DELETE":
            content.delete()
            return Response({"message": "Content Deleted"}, status=status.HTTP_204_NO_CONTENT)

        
    elif request.user.is_superuser:
        if request.method == "PUT":
            serializer = ContentSerializer( content, data=content_data)
            if serializer.is_valid():
                content = serializer.save()
                if 'categories' in data and data['categories'] is not None:
                    content.categories.clear() 
                    content.categories.add(*categories)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == "DELETE":
            content.delete()
            return Response({"message": "Content Deleted"}, status=status.HTTP_204_NO_CONTENT)
 
    else:
        return Response({"error": "You cannot modify this content"}, status=status.HTTP_403_FORBIDDEN)
        
            
        
        

                

       
        
        
        

        
    
        

        
    
    
    
    
    
    




