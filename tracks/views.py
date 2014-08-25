import json
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Track
# Create your views here.

def track_view(request, title):

    track = get_object_or_404(Track, title=title)
    data = {
        'title' : track.title,
        'order' : track.order,
        'album' : serializers.serialize('json', [track.album]),
        'artist' : {
            'name' : track.artist.first_name,
            'bio' : track.artist.biography,
        }
    }


   # json_data = json.dumps(data)

    #return HttpResponse(json_data, content_type="application/json")
    return render(request,"track.html",{'tracks': track})