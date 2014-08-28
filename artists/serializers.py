from rest_framework import serializers

from .models import Artist

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    es_parrel_1 = serializers.SerializerMethodField('es_parrel_2')



    def es_parrel_2(self, obj):
        return obj.es_parrel()
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'es_parrel_1')