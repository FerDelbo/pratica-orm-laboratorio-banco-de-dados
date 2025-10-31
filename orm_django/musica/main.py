# Configuracao de ambiente
import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm_django.settings')
django.setup()


from musica.models import Musica, Artista, Usuario, Playlist, MusicaPlaylist
print("===CREATE===")
# Usuario: nome e plano
usuario1 = Usuario.objects.create(nome="Fernando", plano="Premium")
# Artista: nome
artista1 = Artista.objects.create(nome="Andre")
# Musica: titulo, artista e duracao
musica1 = Musica.objects.create(titulo="Queen", artista=artista1, duracao=322)
# Playlist: nome e usuario
playlist1 = Playlist.objects.create(nome="As melhores do fernando", id_usuario=usuario1)
# musica_playlist: musica e playlist
musica_playlist1 = MusicaPlaylist.objects.create(id_playlist=playlist1, id_musica=musica1) 
print("===READ===")
usuarios = Usuario.objects.all()
# artistas = Artista.objects.all()
# musicas = Musica.objects.all()
# playlists = Playlist.objects.all()
# musica_com_playlist = MusicaPlaylist.objects.all()
for i in usuarios:
    print(i.nome)

#Salvar tudo
usuario1.save()
artista1.save()
musica1.save()
playlist1.save()
musica_playlist1.save()