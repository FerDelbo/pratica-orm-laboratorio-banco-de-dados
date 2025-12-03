# Configuracao de ambiente
import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm_django.settings')
django.setup()

from musica.models import Musica, Artista, Usuario, Playlist, MusicaPlaylist

# função para listar todas as Playlists de um USUARIO específico, usando o username como filtro 
# Deve retorno Nome da playlist e data de criação
def listar_playlists_usuario(username):
    usuario = Usuario.objects.get(username=username)
    playlists = Playlist.objects.filter(usuario_id=usuario)
    for playlist in playlists:
        print(f'Nome da Playlist: {playlist.nome}, Data de Criação: {playlist.data_criacao}')
    return playlists

print("==Teste 1==")
print(listar_playlists_usuario('Pablo'))

# Encontre todas as Músicas que pertencem a qualquer Playlist
#  criada por um USUARIO específico e cujo Artista seja Queen

def listar_musicas_playlists_usuario_artista(username, nome_artista):
    usuario = Usuario.objects.get(username=username)
    artista = Artista.objects.get(nome=nome_artista)
    playlists = Playlist.objects.filter(usuario_id=usuario)
    musicas = Musica.objects.filter(musicaplaylist__playlist_id__in=playlists, artista=artista).distinct()
    for musica in musicas:
        print(f'Título da Música: {musica.titulo}, Artista: {musica.artista.nome}')
    return musicas

print("==Teste 2==")
print(listar_musicas_playlists_usuario_artista('Josue', 'Queen'))
# Liste o nome de todas as Playlists e o número total de Músicas que cada uma contém. 
# A listagem deve ser ordenada da Playlist mais longa para a mais curta.

from django.db.models import Count
def listar_playlists_com_numero_musicas():
    playlists = Playlist.objects.annotate(num_musicas=Count('musicaplaylist__musica_id')).order_by('-num_musicas')
    for playlist in playlists:
        print(f'Nome da Playlist: {playlist.nome}, Número de Músicas: {playlist.num_musicas}')
    return playlists

print("==Teste 3==")
print(listar_playlists_com_numero_musicas())

# Identifique e liste todos os Artistas que não possuem nenhuma de suas Músicas
#  adicionadas a nenhuma Playlist no sistema. 
def listar_artistas_sem_musicas_em_playlists():
    artistas = Artista.objects.exclude(musica__musicaplaylist__isnull=False)
    for artista in artistas:
        print(f'Artista: {artista.nome}')
    return artistas

print("==Teste 4==")
print(listar_artistas_sem_musicas_em_playlists())

