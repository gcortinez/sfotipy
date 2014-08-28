from django.test import TestCase
from django.test import Client
# Create your tests here.

from .models import Artist

from tracks.models import Track
from albums.models import Album


class TestArtists(TestCase):

    def setUp(self):
        self.artist = Artist.objects.create(first_name='david', last_name='bowie')
        self.album = Album.objects.create(title="heroes", artist=self.artist)
        self.track = Track.objects.create(title="heroes", artist=self.artist, album=self.album, order=0, track_file="media/sa")

    def test_usuario_logueado(self):
        res = self.client.get('/tracks/%s/' % self.track.title)
        self.assertEqual(res.status_code, 302)

    def test_existe_vista(self):
        client = Client()
        id_viejo = self.artist.id
        self.artist.delete()
        res = client.get('/artist/%d/' % id_viejo)
        self.assertEqual(res.status_code, 404)
