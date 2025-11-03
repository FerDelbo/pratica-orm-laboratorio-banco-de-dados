from django.db import models

class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False, unique=True)
    nacionalidade = models.CharField(max_length=100, default="Desconhecida")

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username

class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Adicionar PK composta 
        constraints = [
            models.UniqueConstraint(fields=['playlist_id', 'usuario'], name='pk_playlist')
        ]
    def __str__(self):
        return f"Playlist: {self.nome} do usuario: {self.usuario.username}"


class Musica(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255, null=False)
    duracao_segundos = models.IntegerField(help_text="Duração em segundos", null=False)
    artista = models.ForeignKey('Artista', on_delete=models.RESTRICT, )

    class Meta:
        # Check de duracao deve ser positiva
        constraints =[
            models.CheckConstraint(check=models.Q(duracao_segundos__gt=0), name='duracao_positiva')
        ]

    def __str__(self):
        return f"{self.titulo} por {self.artista.nome}"

    
class MusicaPlaylist(models.Model):
    musica = models.ForeignKey('Musica', on_delete=models.CASCADE, null=False)
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE, unique=False, null=False)
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, unique=False, null=False)
    ordem_na_playlist = models.IntegerField(null=False)

    class Meta:
        # Adicionar PK composta 
        constraints = [
            models.UniqueConstraint(fields=['musica', 'playlist', 'usuario'], name='pk_musica_playlist'),
            models.UniqueConstraint(fields=['playlist', 'usuario', 'ordem_na_playlist'], name='unique_ordem_playlist')
        ]

    def __str__(self):
        return f"Música: {self.id_musica.titulo} na Playlist: {self.id_playlist.nome}"
