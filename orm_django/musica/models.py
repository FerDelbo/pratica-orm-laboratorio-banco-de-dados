from django.db import models

class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, unique=True)
    nacionalidade = models.CharField(max_length=100, default="Desconhecida")

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=255, unique=True)


class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='usuario_id', null=False)
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['playlist_id', 'usuario_id'], name='pk_playlist_usuario')
        ]

class Musica(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255, null=False)
    duracao_segundos = models.IntegerField(help_text="Duração em segundos", null=False)
    artista = models.ForeignKey('Artista', on_delete=models.RESTRICT)

    class Meta:
        # Check de duracao deve ser positiva
        constraints =[
            models.CheckConstraint(check=models.Q(duracao_segundos__gt=0), name='duracao_positiva')
        ]

    
class MusicaPlaylist(models.Model):
    pk = models.CompositePrimaryKey("musica_id", "playlist_id", "usuario_id")
    musica_id = models.ForeignKey('Musica', on_delete=models.CASCADE, null=False)
    playlist_id = models.IntegerField(null=False)
    usuario_id = models.IntegerField(null=False)
    playlist = models.ForeignObject(
        'Playlist',
        on_delete=models.CASCADE,
        from_fields=['playlist_id', 'usuario_id'],
        to_fields=['playlist_id', 'usuario_id']
    )
    ordem_na_playlist = models.IntegerField(null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['ordem_na_playlist', 'playlist_id', 'usuario_id'], name='pk_musica_playlist_usuario')
        ]