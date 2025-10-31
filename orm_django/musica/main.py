from models import Musica, Artista, Usuario, Playlist, MusicaPlaylist
# Usuario: nome e plano
usuario1 = Usuario.objects.create(nome="Fernando", plano="Premium")
# Artista: nome
artista1 = Artista.objects.create(nome="Andre")
# Musica: titulo, artista e duracao
musica1 = Musica.objects.create(titulo="")
# Playlist: nome e usuario
playlist1 = Playlist.objects.create()
# musica_playlist: musica e playlist
musica_playlist1 = MusicaPlaylist.objects.create() 