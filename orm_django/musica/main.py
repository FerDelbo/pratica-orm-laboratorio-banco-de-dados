# Configuracao de ambiente
import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm_django.settings')
django.setup()

from musica.models import Musica, Artista, Usuario, Playlist, MusicaPlaylist

# # Popular banco de dados
# queen = Artista.objects.create(nome='Queen', nacionalidade='Britânica') #1
# queen.save()
# led_zeppelin = Artista.objects.create(nome='Led Zeppelin', nacionalidade='Britânica') # 2
# led_zeppelin.save()
# acdc = Artista.objects.create(nome='AC/DC', nacionalidade='Australiana') # 3
# acdc.save()
# banda_x = Artista.objects.create(nome='Banda X (Pop)', nacionalidade='Brasileira') # 3
# banda_x.save()

# pablo = Usuario.objects.create(username='Pablo', email='pablo@aluno.com') # 1
# pablo.save()
# josue = Usuario.objects.create(username='Josue', email='josue@aluno.com') # 2
# josue.save()
# alexandre = Usuario.objects.create(username='Alexandre', email='alexandre@aluno.com') # 3
# alexandre.save()

# # artista id =1 -> queen
# bohemian = Musica.objects.create(titulo='Bohemian Rhapsody', duracao_segundos=354, artista=queen)
# bohemian.save()
# we_will_rock_you = Musica.objects.create(titulo='We Will Rock You', duracao_segundos=160, artista=queen)
# we_will_rock_you.save()
# #artista_id=2 -> artista=led_zeppelin
# stairway = Musica.objects.create(titulo='Stairway to Heaven', duracao_segundos=482, artista=led_zeppelin)
# stairway.save()
# #artista_id=3 -> artista=acdc
# back_in_black = Musica.objects.create(titulo='Back In Black', duracao_segundos=255, artista=acdc)
# back_in_black.save()
# thunderstruck = Musica.objects.create(titulo='Thunderstruck', duracao_segundos=292, artista=acdc)
# thunderstruck.save()('usuario', models.ForeignKey(db_column='usuario_id', on_delete=django.db.models.deletion.CASCADE, to='musica.usuario')),

# #artista_id=4 -> artista=banda_x
# pop_br = Musica.objects.create(titulo='Musica Pop Brasileira', duracao_segundos=180, artista=banda_x)
# pop_br.save()

# pablo = Usuario.objects.get(id=1)
# josue = Usuario.objects.get(id=2)

# bohemian = Musica.objects.get(id=1)
# stairway = Musica.objects.get(id=2)
# back_in_black = Musica.objects.get(id=3)
# we_will_rock_you = Musica.objects.get(id=4)

# thunderstruck = Musica.objects.get(id=6)


# p1_pablo = Playlist.objects.create(playlist_id=1, usuario_id=pablo, nome='Rock do Pablo')
# p1_pablo.save()
# p1_josue = Playlist.objects.create(playlist_id=2, usuario_id=josue, nome='Baladas do Josue')
# p1_josue.save()
# p2_pablo = Playlist.objects.create(playlist_id=3, usuario_id=pablo, nome='Heavy Riffs')
# p2_pablo.save()

# mp1 = MusicaPlaylist.objects.create(
#     musica_id=bohemian,       # musica_id 1
#     playlist_id=1,
#     usuario_id=pablo.id,   # usuario_id 1
#     ordem_na_playlist=1
# )
# mp1.save()
# mp2 = MusicaPlaylist.objects.create(
#     musica_id=back_in_black,  # musica_id 3
#     playlist_id=1,
#     usuario_id=pablo.id,
#     ordem_na_playlist=2
# )
# mp2.save()
# mp3 = MusicaPlaylist.objects.create(
#     musica_id=we_will_rock_you, # musica_id 4
#     playlist_id=1,
#     usuario_id=pablo.id,
#     ordem_na_playlist=3
# )
# mp3.save()
# # Playlist (2, 2): 'Baladas do Josue'
# mp4 = MusicaPlaylist.objects.create(
#     musica_id=stairway,        # musica_id 2
#     playlist_id=2,
#     usuario_id=josue.id,   # usuario_id 2
#     ordem_na_playlist=1
# )
# mp4.save()
# # Playlist (3, 1): 'Heavy Riffs'
# mp5 = MusicaPlaylist.objects.create(
#     musica_id=back_in_black,  # musica_id 3
#     playlist_id=3,
#     usuario_id=pablo.id,   # usuario_id 1
#     ordem_na_playlist=1
# )
# mp5.save()
# mp6 = MusicaPlaylist.objects.create(
#     musica_id=thunderstruck,  # musica_id 6
#     playlist_id=3,
#     usuario_id=pablo.id,
#     ordem_na_playlist=2
# )
# mp6.save()

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
a1.save() 

print("===DELETE===")
# a1.delete()

# print("\n===CRUD Musica===\n")

# print("===CREATE===")
# m1 = Musica.objects.create(titulo="Believer", duracao_segundos=204, artista=artista_id)
# m1.save() # Salvar no banco de dados

# print("===READ===")
# musica_id = Musica.objects.get(id=7) # Pegar a "Believer"
# print("Música:", musica_id.titulo)

# print("===UPDATE===")
# m1.duracao_segundos = 210
# m1.save() # Atualizar no banco de dados

# print("===DELETE===")
# # m1.delete() # Deletar do banco de dados

# # 2 Criar usuario e playlist
# p1 = Playlist.objects.create(playlist_id=4, nome="Clássicos do Alexandre", usuario=Usuario.objects.get(id=3))
# p1.save()
# p1 = Playlist.objects.get(playlist_id=4, usuario=3)
# # # Adicionar musicas na playlist
# mp1 = MusicaPlaylist.objects.create(ordem_na_playlist=1, musica=Musica.objects.get(id=1), playlist=p1, usuario=Usuario.objects.get(id=3))
# mp1.save()
# mp2 = MusicaPlaylist.objects.create(ordem_na_playlist=2, musica=Musica.objects.get(id=2), playlist=p1, usuario=Usuario.objects.get(id=3))
# mp2.save()

# # 3.1 Criar função para criar playlist com musicas
# def adicionar_musica_na_playlist(usuario_id, nome_playlist, musica):
#     # usuario = Usuario.objects.get(id=usuario_id)
#     play = Playlist.objects.get(nome=nome_playlist, usuario=usuario_id)
#     if not play:
#         print("Playlist não existe. Criando nova playlist.")
#         play = Playlist.objects.create(nome=nome_playlist, usuario=Usuario.objects.get(id=usuario_id))
#         play.save()
#     ordem = MusicaPlaylist.objects.filter(playlist=play, usuario=usuario_id).count() + 1
#     mp = MusicaPlaylist.objects.create(ordem_na_playlist=ordem, musica=musica, playlist=play, usuario=Usuario.objects.get(id=usuario_id))
#     mp.save()
#     print(f"Música {musica.titulo} adicionada à playlist {nome_playlist}.")

# #3.2 Deletar musica da playlist
# def remover_musica_da_playlist(usuario_id, nome_playlist, musica):
#     play = Playlist.objects.get(nome=nome_playlist, usuario=usuario_id)
#     if not play:
#         print("Playlist não existe.")
#         return
#     mp = MusicaPlaylist.objects.get(musica=musica, playlist=play, usuario=usuario_id)
#     if not mp:
#         print("Música não encontrada na playlist.")
#         return
#     mp.delete()
#     print(f"Música {musica.titulo} removida da playlist {nome_playlist}.")

# adicionar_musica_na_playlist(
#     usuario_id=3, #Alexandre
#     nome_playlist="Clássicos do Alexandre",
#     musica=Musica.objects.get(id=7)
# )

# remover_musica_da_playlist(
#     usuario_id=3, #Alexandre
#     nome_playlist="Clássicos do Alexandre",
#     musica=Musica.objects.get(id=7)
# )
