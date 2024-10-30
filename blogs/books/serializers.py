from rest_framework import serializers
from .models import Book, Author, Publisher
from datetime import timedelta
from django.utils import timezone


class AuthorSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Author
        fields = '__all__'

      
class PublisherSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Publisher
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer
    publisher = PublisherSerializer
      
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate(self, attrs):
        title = attrs.get('title')
        description = attrs.get('description')
        publication_date = attrs.get('publication_date')
        price = attrs.get('price')
        
        if title and len(title) > 100:
            raise serializers.ValidationError('Title cannot exceed 100 characters')
        
        # Description must be at least 10 words
        if description and len(description.split()) < 10:
            raise serializers.ValidationError('Description must be of at least 10 words')
            
        # Publication date must be at least 1 month old
        one_month_ago = timezone.now() - timedelta(days=30)
        if publication_date and publication_date > one_month_ago.date():
            raise serializers.ValidationError('Publication date must be at least one month old')
        
        # Price must be between 100 and 10000
        if price and (price < 100 or price > 10000):
            raise serializers.ValidationError('Price must be between 100 and 10000')
        
        return attrs
    
    def create(self, validated_data):
        author = validated_data.pop('author')
        author_serializer = AuthorSerializer(data=author)
        if author_serializer.is_valid():
            author_instance = author_serializer.save()
            validated_data['author'] = author_instance
            
        
        publisher = validated_data.pop('publisher')
        publisher_serializer = AuthorSerializer(data=publisher)
        if publisher_serializer.is_valid():
            publisher_instance = publisher_serializer.save()
            validated_data['publisher'] = publisher_instance
        
        return super().create(validated_data)
            
    def update(self, instance, validated_data):
        validated_data['updated at'] = timezone.now()
        
        return super().update(instance, validated_data)
        
        
