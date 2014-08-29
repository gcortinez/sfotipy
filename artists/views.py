from django.shortcuts import render

from django.views.generic.detail import  DetailView
from .models import Artist
# Create your views here.

from rest_framework import viewsets

from .serializers import ArtistSerializer

class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'artist'
    def get_template_names(self):
        return 'artist.html'


class ArtistViewSet(viewsets.ModelViewSet):
    model = Artist
    serializer_class = ArtistSerializer

    paginate_by = 1
    filter_fields = ('first_name',)

