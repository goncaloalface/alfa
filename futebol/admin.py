from django.contrib import admin
from .models import Clube,Noticia, JogosRecentesLigaCampeoes, JogosRecentesLigaPortuguesa, MelhoresAssistencias, \
    MelhoresMarcadoresEuropa,MelhoresMarcadoresPortugal, classificacao, videodasemana,Comment

admin.site.register(Clube)
admin.site.register(Noticia)
admin.site.register(JogosRecentesLigaCampeoes)
admin.site.register(JogosRecentesLigaPortuguesa)
admin.site.register(MelhoresAssistencias)
admin.site.register(MelhoresMarcadoresEuropa)
admin.site.register(MelhoresMarcadoresPortugal)
admin.site.register(classificacao)
admin.site.register(videodasemana)
admin.site.register(Comment)
