from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# Serializer for the Book model.
# Handles serialization of all fields and custom validation for publication_year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure publication_year is not in the future.
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for the Author model.
# Includes the name field and a nested BookSerializer to serialize related books.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer for the related books.
    # This allows retrieving an author along with all their books dynamically.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
