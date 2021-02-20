from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=3000)
    autor = models.CharField(max_length=50)
    imagem = models.CharField(max_length=2000)
    breve = models.CharField(max_length=1500)

    def __str__(self):
        return self.titulo + ' - ' + self.autor


class Clube(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    imagem = models.CharField(max_length=2000)
    historia = models.CharField(max_length=5000)
    wiki = models.CharField(max_length=300)

    def __str__(self):
        return self.nome + ' - ' + self.sigla



class JogosRecentesLigaPortuguesa(models.Model):
    EquipaDaCasa = models.CharField(max_length=100)
    resultado = models.CharField(max_length=6)
    EquipaDaFora = models.CharField(max_length=100)
    ImagemDaCasa30x30 = models.CharField(max_length=2000)
    ImagemDaFora30x30 = models.CharField(max_length=2000)

    def __str__(self):
        return self.EquipaDaCasa + ' - ' + self.resultado + ' - ' + self.EquipaDaFora


class JogosRecentesLigaCampeoes(models.Model):
    EquipaDaCasa = models.CharField(max_length=100)
    resultado = models.CharField(max_length=6)
    EquipaDaFora = models.CharField(max_length=100)
    ImagemDaCasa30x30 = models.CharField(max_length=2000)
    ImagemDaFora30x30 = models.CharField(max_length=2000)

    def __str__(self):
        return self.EquipaDaCasa + ' - ' + self.resultado + ' - ' + self.EquipaDaFora


class MelhoresMarcadoresPortugal(models.Model):
    nome = models.CharField(max_length=100)
    clube = models.CharField(max_length=100)
    pontos = models.CharField(max_length=100)
    texto = models.CharField(max_length=1000)
    imagem = models.CharField(max_length=2000)

    def __str__(self):
        return self.nome + ' - ' + self.pontos


class MelhoresAssistencias(models.Model):
    nome = models.CharField(max_length=100)
    clube = models.CharField(max_length=100)
    pontos = models.CharField(max_length=100)
    texto = models.CharField(max_length=1000)
    imagem = models.CharField(max_length=2000)

    def __str__(self):
        return self.nome + ' - ' + self.pontos


class MelhoresMarcadoresEuropa(models.Model):
    nome = models.CharField(max_length=100)
    clube = models.CharField(max_length=100)
    pontos = models.CharField(max_length=100)
    texto = models.CharField(max_length=1000)
    imagem = models.CharField(max_length=2000)

    def __str__(self):
        return self.nome + ' - ' + self.pontos


class classificacao(models.Model):
    clube = models.CharField(max_length=100)
    imagem = models.CharField(max_length=100)
    pontos = models.CharField(max_length=100)
    jogos = models.CharField(max_length=100)
    vitorias = models.CharField(max_length=100)
    empates = models.CharField(max_length=100)
    derrotas = models.CharField(max_length=100)
    golos_marcados = models.IntegerField()
    golos_sofridos = models.IntegerField()

    def __str__(self):
        return self.clube + ' - ' + self.pontos


class videodasemana(models.Model):
    url = models.CharField(max_length=4000)
    texto = models.CharField(max_length=3000)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    #noticia = models.ForeignKey(Noticia)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)
