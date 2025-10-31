from django.db import models

class Musica(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, null=False)
    artista = models.ForeignKey('Artista', on_delete=models.CASCADE, )
    duracao = models.IntegerField(help_text="Duração em segundos", null=False)

    class Meta:
        # Check de duracao deve ser positiva
        constraints =[
            models.CheckConstraint(check=models.Q(duracao__gt=0), name='duracao_positiva')
        ]

    def __str__(self):
        return f"{self.titulo} por {self.artista}"

class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    plano = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Playlist(models.Model):
    id_playlist = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    class Meta:
        # Adicionar PK composta 
        constraints = [
            models.UniqueConstraint(fields=['id_usuario', 'id_playlist'], name='pk_playlist')
        ]
    def __str__(self):
        return f"Playlist: {self.nome} do usuario: {self.id_usuario.nome}"
    
class MusicaPlaylist(models.Model):
    id_musica = models.ForeignKey('Musica', on_delete=models.CASCADE)
    id_playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)

    class Meta:
        # Adicionar PK composta 
        constraints = [
            models.UniqueConstraint(fields=['id_musica', 'id_playlist'], name='pk_musica_playlist')
        ]

    def __str__(self):
        return f"Música: {self.id_musica.titulo} na Playlist: {self.id_playlist.nome}"
