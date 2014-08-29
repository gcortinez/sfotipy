import json
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Track
from rest_framework import viewsets
import time

from django.core.cache import cache
from django.views.decorators.cache import cache_page
# Create your views here.


#@login_required()
#@cache_page(60)
def track_view(request, title):
    #data_cache = cache.get('data_%s' % title)
    track = get_object_or_404(Track, title=title)

    #if data_cache is None:
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
    time.sleep(5)
    #cache.set('data_%s' % title, data)
    #return HttpResponse(json_data, content_type="application/json")
    return render(request,"track.html",{'tracks': track})

class TrackViewSet(viewsets.ModelViewSet):
    model = Track