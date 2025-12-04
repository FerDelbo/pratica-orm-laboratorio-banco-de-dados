# Configuracao de ambiente
import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm_django.settings')
django.setup()


from musica.models import Musica, Artista, Usuario, Playlist, MusicaPlaylist

# m = Musica.objects.all()
# for musica in m:
#     print(f'{musica.id} - {musica.titulo} - {musica.duracao_segundos} seg - Artista: {musica.artista.nome}')

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

# Crie uma função para buscar uma Música por seu id e,
#  em uma única operação de consulta (evitando o problema N+1),
#  carregue (fetch) automaticamente todos os detalhes do Artista relacionado.
#  (Foco em Eager Loading ou Fetching Join).
def buscar_musica_com_artista(musica_id):
    musica = Musica.objects.select_related('artista').get(id=musica_id)
    # O select_related acima evita o porblema N+1 pois busca as Musicas com o artista direto
    print(f'Título da Música: {musica.titulo}, Artista: {musica.artista.nome}, Nacionalidade: {musica.artista.nacionalidade}')
    return musica

print("==Teste 5==")
print(buscar_musica_com_artista(1))

# Para cada PLAYLIST no sistema, calcule e retorne o tempo total de reprodução
#  (soma de duracao_segundos de todas as músicas). 
# A saída deve listar o nome da Playlist, o username do Dono e o tempo total
#  de reprodução. (Foco em agregação SUM e GROUP BY sobre o N:N).

def listar_tempo_total_playlists():
    from django.db.models import Sum

    qs = Playlist.objects.annotate(
        tempo_total=Sum('musicaplaylist__musica_id__duracao_segundos')
    )
    
    resultados = []
    for p in qs:
        tempo = p.tempo_total or 0
        dono = getattr(p, 'usuario_id', None)   # FK no model chama-se `usuario_id`
        username = dono.username if dono else None
        print(f'Nome: {p.nome}, Dono: {username}, Tempo total: {tempo} segundos')
        resultados.append({'nome': p.nome, 'username': username, 'tempo_total': tempo})

    return resultados

print("==Teste 6==")
print(listar_tempo_total_playlists())

# Liste todas as Músicas cujo tempo de duração (duracao_segundos)
#  é menor que o tempo de duração médio de todas as músicas do seu próprio Artista
#  (ex: listar músicas do AC/DC que são mais curtas que a média do AC/DC).
#  (Foco em subconsultas ou Window Functions se o ORM suportar).
def listar_musicas_abaixo_media_artista():
    from django.db.models import Avg, OuterRef, Subquery, F

    subquery = Musica.objects.filter(artista=OuterRef('artista')).values('artista').annotate(media_duracao=Avg('duracao_segundos')).values('media_duracao')
    musicas = Musica.objects.annotate(media_duracao_artista=Subquery(subquery)).filter(duracao_segundos__lt=F('media_duracao_artista'))
    for musica in musicas:
        print(f'Título da Música: {musica.titulo}, Duração: {musica.duracao_segundos}, Média do Artista: {musica.media_duracao_artista}')
    return musicas

print("==Teste 7==")
print(listar_musicas_abaixo_media_artista())

# Liste o título de todas as Músicas na playlist 'Rock do Pablo',
#  incluindo a ordem_na_playlist de cada música.

def listar_musicas_na_playlist(nome_playlist):
    playlist = Playlist.objects.get(nome=nome_playlist)
    musicas_playlist = MusicaPlaylist.objects.filter(playlist=playlist).select_related('musica_id').order_by('ordem_na_playlist')
    for mp in musicas_playlist:
        print(f'Ordem: {mp.ordem_na_playlist}, Título da Música: {mp.musica_id.titulo}')
    return musicas_playlist

print("==Teste 8==")
# print(listar_musicas_na_playlist('Rock do Pablo'))
print(listar_musicas_na_playlist('Baladas do Josue'))

# Encontre o username do Usuário que é o dono da Playlist que contém a MUSICA 'Bohemian Rhapsody'.
#  O filtro deve começar pela MUSICA e navegar de volta para o USUARIO.
def encontrar_dono_playlist_por_musica(titulo_musica):
    musica = Musica.objects.get(titulo=titulo_musica)
    musicas_playlist = MusicaPlaylist.objects.filter(musica_id=musica).select_related('playlist__usuario_id')
    donos = set()
    for mp in musicas_playlist:
        dono = mp.playlist.usuario_id
        donos.add(dono.username)
        print(f'Username do Dono da Playlist: {dono.username}')
    return donos

print("==Teste 9==")
# Musica Pop Brasileira
# encontrar_dono_playlist_por_musica('Bohemian Rhapsody')
encontrar_dono_playlist_por_musica('Musica Pop Brasileira')

# Liste todos os Artistas e seu ranking baseado no número de Playlists
#  em que suas músicas estão presentes (o Artista com músicas na maior
#  quantidade de playlists fica em 1º).

def listar_ranking_artistas_por_playlists():
    from django.db.models import Count
    artistas = Artista.objects.annotate(num_playlists=Count('musica__musicaplaylist__playlist_id', distinct=True)).order_by('-num_playlists')
    for artista in artistas:
        print(f'Artista: {artista.nome}, Número de Playlists: {artista.num_playlists}')
    return artistas

print("==Teste 10==")
print(listar_ranking_artistas_por_playlists())



def listar_musicas_led_mais_longas_que_queen_max():
    from django.db.models import Max, Subquery

    subq = (
        Musica.objects
        .filter(artista__nome='Queen')
        .values('artista')
        .annotate(max_dur=Max('duracao_segundos'))
        .values('max_dur')
    )
    qs = Musica.objects.filter(artista__nome='Led Zeppelin', duracao_segundos__gt=Subquery(subq))
    resultados = []
    for m in qs:
        print(f'Título: {m.titulo}, Duração: {m.duracao_segundos}, Artista: {m.artista.nome}')
        resultados.append(m)
    return resultados


print("==Teste 11==")
listar_musicas_led_mais_longas_que_queen_max()

#  Implemente uma função que mova uma MUSICA de uma PLAYLIST
#  para outra PLAYLIST (ambas do mesmo USUARIO),
#  garantindo que o processo seja Atômico (ou tudo acontece ou nada acontece).

# def mover_musica_entre_playlists(usuario_id, musica_id, playlist_origem_id, playlist_destino_id):
#     from django.db import transaction

#     try:
#         with transaction.atomic():
#             mp_origem = MusicaPlaylist.objects.get(
#                 musica_id=musica_id,
#                 playlist_id=playlist_origem_id,
#                 usuario_id=usuario_id
#             )
#             # Verifica se a música já está na playlist de destino
#             if MusicaPlaylist.objects.filter(
#                 musica_id=musica_id,
#                 playlist_id=playlist_destino_id,
#                 usuario_id=usuario_id
#             ).exists():
#                 print("A música já está na playlist de destino.")
#                 return

#             # Remove da playlist de origem
#             mp_origem.delete()

#             # Adiciona à playlist de destino
#             ordem_destino = MusicaPlaylist.objects.filter(
#                 playlist_id=playlist_destino_id,
#                 usuario_id=usuario_id
#             ).count() + 1

#             mp_destino = MusicaPlaylist.objects.create(
#                 musica_id=musica_id,
#                 playlist_id=playlist_destino_id,
#                 usuario_id=usuario_id,
#                 ordem_na_playlist=ordem_destino
#             )
#             mp_destino.save()
#             print("Música movida com sucesso.")
#     except Exception as e:
#         print(f"Erro ao mover música: {e}")

def mover_musica_entre_playlists(usuario_id, musica_id, playlist_origem_id, playlist_destino_id):
    from django.db import transaction
    try:
        with transaction.atomic():
            # busca instâncias
            musica_obj = Musica.objects.get(id=musica_id)
            mp_origem = MusicaPlaylist.objects.select_related('playlist').get(
                musica_id=musica_obj,
                playlist_id=playlist_origem_id,
                usuario_id=usuario_id
            )

            # valida proprietário das playlists (segurança)
            if mp_origem.playlist.usuario_id.id != usuario_id:
                print("Playlist de origem não pertence ao usuário informado.")
                return

            # verifica existência na playlist destino
            if MusicaPlaylist.objects.filter(
                musica_id=musica_obj,
                playlist_id=playlist_destino_id,
                usuario_id=usuario_id
            ).exists():
                print("A música já está na playlist de destino.")
                return

            # remove da origem
            mp_origem.delete()

            # calcula próxima ordem e cria novo registro — passe a instância de Musica
            ordem_destino = MusicaPlaylist.objects.filter(
                playlist_id=playlist_destino_id,
                usuario_id=usuario_id
            ).count() + 1

            mp_destino = MusicaPlaylist.objects.create(
                musica_id=musica_obj,          # instância obrigatória
                playlist_id=playlist_destino_id,
                usuario_id=usuario_id,
                ordem_na_playlist=ordem_destino
            )
            print("Música movida com sucesso.")
    except Musica.DoesNotExist:
        print("Música não encontrada.")
    except MusicaPlaylist.DoesNotExist:
        print("Registro da música na playlist de origem não encontrado.")
    except Exception as e:
        print(f"Erro ao mover música: {e}")
# ...existing code...

print("==Teste 12==")

mover_musica_entre_playlists(
    usuario_id=1, # Pablo
    musica_id=1, # Bohemian Rhapsody
    playlist_origem_id=1, # Rock do Pablo
    playlist_destino_id=3 # Heavy Riffs
)


