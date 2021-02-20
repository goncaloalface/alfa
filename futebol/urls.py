from django.conf.urls import url
from . import views

app_name = 'futebol'

urlpatterns = [

    # /futebol/
    url(r'^$', views.index, name='index'),
    #/futebol/noticias/
    url(r'noticias/$', views.noticia, name='noticias'),
    # /futebol/about/
    url(r'about/$', views.about, name='about'),
     # /futebol/contactos/
    url(r'contactos/$', views.contactos, name='contactos'),
    # /futebol/clubes/
    url(r'clubes/$', views.clubes, name='clubes'),
    # /futebol/clubes/12/

    # /futebol/agenda/
    url(r'agenda/$', views.agenda, name='agenda'),
    # /futebol/estatisticas/
    url(r'estatisticas/$', views.estatisticas, name='estatisticas'),

    url(r'^(?P<noticia_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'clubes/(?P<clube_id>[0-9]+)/$', views.detailClube, name='detailClube'),

    url(r'login/$', views.login_view, name='login'),
    url(r'logout/$', views.logout_view, name='logout'),
    url(r'register/$', views.register_view, name='register'),

]