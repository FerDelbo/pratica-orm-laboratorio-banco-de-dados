# Configuracao de ambiente
import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm_django.settings')
django.setup()


from musica.models import Musica, Artista, Usuario, Playlist, MusicaPlaylist
# print("===CREATE===")
# # Usuario: nome e plano
usuario1 = Usuario.objects.create(nome="Gabriel", plano="Free")
# # Artista: nome
# artista1 = Artista.objects.create(nome="Andre")
# # Musica: titulo, artista e duracao
# musica1 = Musica.objects.create(titulo="Queen", artista=artista1, duracao=322)
# # Playlist: nome e usuario
# playlist1 = Playlist.objects.create(nome="As melhores do fernando", id_usuario=usuario1)
# # musica_playlist: musica e playlist
# musica_playlist1 = MusicaPlaylist.objects.create(id_playlist=playlist1, id_musica=musica1) 

# #Salvar o conteudo no banco de dados
usuario1.save()
# artista1.save()
# musica1.save()
# playlist1.save()
# musica_playlist1.save()

print("===READ===")
usuarios = Usuario.objects.all()
artistas = Artista.objects.all()
musicas = Musica.objects.all()
playlists = Playlist.objects.all()
musica_com_playlist = MusicaPlaylist.objects.all()
for i in usuarios:
    print("Usuário:",i.nome)

for i in artistas:
    print("Artista:",i.nome)

for i in musicas:
    print("Música:",i.titulo)

for i in playlists:
    print("Playlist:",i.nome)

for i in musica_com_playlist:
    print("Música na Playlist:",i.id_musica.titulo, "na playlist", i.id_playlist.nome)

print("===UPDATE===")
# Maneira com "SQL"
usuario_to_update = Usuario.objects.get(id=2)
usuario_to_update.plano = "Gratuito"
usuario_to_update.save()
# Maneira com objeto
usuario1.plano = "Premium"
usuario1.save()

print("===DELETE===")
# Maneira com "SQL"
usuario_to_delete = Usuario.objects.get(id=2)
usuario_to_delete.delete()
# Maneira com objeto
usuario1.delete()
