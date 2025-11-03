# Configuracao de ambiente
import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm_django.settings')
django.setup()


from musica.models import Musica, Artista, Usuario, Playlist, MusicaPlaylist
#1 CRUD artista e musica
print("===CRUD Artista===")
print("===CREATE===")
a1 = Artista.objects.create(nome="Imagine Dragons", nacionalidade="EUA")
a1.save() # Salvar no banco de dados
print("===READ===")
artista_id = Artista.objects.get(id=5) # Pegar o "Imagine Dragons"
print("Artista:", artista_id.nome)
print("===UPDATE===")
a1.nacionalidade = "Estadunidense"
a1.save() # Atualizar no banco de dados
# print("===DELETE===")
# a1.delete() # Deletar do banco de dados
print("===CRUD Musica===")
print("===CREATE===")
m1 = Musica.objects.create(titulo="Believer", duracao_segundos=204, artista=artista_id)
m1.save() # Salvar no banco de dados
print("===READ===")
musica_id = Musica.objects.get(id=7) # Pegar a "Believer"
print("Música:", musica_id.titulo)
print("===UPDATE===")
m1.duracao_segundos = 210
m1.save() # Atualizar no banco de dados
# print("===DELETE===")
# m1.delete() # Deletar do banco de dados

# 2 Criar usuario e playlist
p1 = Playlist.objects.create(playlist_id=4, nome="Clássicos do Alexandre", usuario=Usuario.objects.get(id=3))
p1.save()
p1 = Playlist.objects.get(playlist_id=4, usuario=3)
# # Adicionar musicas na playlist
mp1 = MusicaPlaylist.objects.create(ordem_na_playlist=1, musica=Musica.objects.get(id=1), playlist=p1, usuario=Usuario.objects.get(id=3))
mp1.save()
mp2 = MusicaPlaylist.objects.create(ordem_na_playlist=2, musica=Musica.objects.get(id=2), playlist=p1, usuario=Usuario.objects.get(id=3))
mp2.save()

# 3.1 Criar função para criar playlist com musicas
def adicionar_musica_na_playlist(usuario_id, nome_playlist, musica):
    # usuario = Usuario.objects.get(id=usuario_id)
    play = Playlist.objects.get(nome=nome_playlist, usuario=usuario_id)
    if not play:
        print("Playlist não existe. Criando nova playlist.")
        play = Playlist.objects.create(nome=nome_playlist, usuario=Usuario.objects.get(id=usuario_id))
        play.save()
    ordem = MusicaPlaylist.objects.filter(playlist=play, usuario=usuario_id).count() + 1
    mp = MusicaPlaylist.objects.create(ordem_na_playlist=ordem, musica=musica, playlist=play, usuario=Usuario.objects.get(id=usuario_id))
    mp.save()
    print(f"Música {musica.titulo} adicionada à playlist {nome_playlist}.")

#3.2 Deletar musica da playlist
def remover_musica_da_playlist(usuario_id, nome_playlist, musica):
    play = Playlist.objects.get(nome=nome_playlist, usuario=usuario_id)
    if not play:
        print("Playlist não existe.")
        return
    mp = MusicaPlaylist.objects.get(musica=musica, playlist=play, usuario=usuario_id)
    if not mp:
        print("Música não encontrada na playlist.")
        return
    mp.delete()
    print(f"Música {musica.titulo} removida da playlist {nome_playlist}.")

adicionar_musica_na_playlist(
    usuario_id=3, #Alexandre
    nome_playlist="Clássicos do Alexandre",
    musica=Musica.objects.get(id=7)
)

remover_musica_da_playlist(
    usuario_id=3, #Alexandre
    nome_playlist="Clássicos do Alexandre",
    musica=Musica.objects.get(id=7)
)
