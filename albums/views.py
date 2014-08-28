from django.shortcuts import render

from rest_framework import viewsets

from .models import Album

# Create your views here.

class AlbumViewSet(viewsets.ModelViewSet):
    model = Album

