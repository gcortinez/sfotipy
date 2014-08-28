from random import choice


frases = ["hola", "prueba", "algo", "frase", "django"]

from tracks.models import Track

def basico(request):
    songs = Track.objects.all()
    song = None

    for t in songs:
        if request.path == t.get_absolute_url():
            song = t
            break
    return {'titulo' : choice(frases), "songs": songs, 'selected_song' : song}