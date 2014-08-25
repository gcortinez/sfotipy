from random import choice


frases = ["hola", "prueba", "algo", "frase", "django"]

from tracks.models import Track

def basico(request):
    tracks = Track.objects.all()
    return {'titulo' : choice(frases), "tracks": tracks}