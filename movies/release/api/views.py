from django.shortcuts import render

from rest_framework import viewsets

from release.api.serializers import BookSerializer, ReleaseSerializer
from release.models import Book, Release

# Create your views here.


# book list
class BookViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
