from release.models import Book, Author, Release
from rest_framework import serializers


# AuthorsSerializers
class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']


# Book Serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'genres']


#
class ReleaseSerializer(serializers.ModelSerializer):
    book = serializers.ReadOnlyField(source='book.name')

    class Meta:
        model = Release
        fields = ['book', 'text', 'release_data', 'authors', 'ratings']
