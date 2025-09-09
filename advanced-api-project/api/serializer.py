from rest_framework import serializers
from .models import Author, Book

# Book serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

        # validate that publication year is not in the future
        def validate_publication_year(self, value):
            if value > 2024:
                raise serializers.ValidationError("Publication year cannot be in the future.")
            return value

# Author serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']

# Nested serializer to include author details in Book serializer
class BookSerializer(serializers.ModelSerializer):
    
    """
    BookSerializer is a ModelSerializer for the Book model that includes a nested representation of related authors.
    The 'author' field uses AuthorSerializer with many=True, indicating a many-to-many or one-to-many relationship,
    and is set to read_only to prevent modification through this serializer. All fields from the Book model are included.
    """

    author = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
