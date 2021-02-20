from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from .models import Noticia, Clube, JogosRecentesLigaCampeoes, JogosRecentesLigaPortuguesa, \
    MelhoresAssistencias, MelhoresMarcadoresEuropa,MelhoresMarcadoresPortugal, classificacao, videodasemana, Comment

from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm, CommentForm

def index(request):
    all_noticias = Noticia.objects.all()
    all_clubes = Clube.objects.all()
    all_campeoes = JogosRecentesLigaCampeoes.objects.all().order_by('-id')[:2]
    all_portuguesa = JogosRecentesLigaPortuguesa.objects.all().order_by('-id')[:4]
    all_melhoresPortugal = MelhoresMarcadoresPortugal.objects.all().order_by('-pontos')[:1]
    all_melhoresEuropa = MelhoresMarcadoresEuropa.objects.all().order_by('-pontos')[:1]
    all_melhoresAssistencias = MelhoresAssistencias.objects.all().order_by('-pontos')[:1]
    all_videodasemana = videodasemana.objects.all()
    all_organize = Noticia.objects.all().order_by('-id')[:3]
    context = {'all_noticias': all_noticias, 'all_clubes': all_clubes, 'all_campeoes':all_campeoes,
               'all_portuguesa': all_portuguesa, 'all_organize':all_organize,
               'all_melhoresPortugal': all_melhoresPortugal, 'all_melhoresEuropa': all_melhoresEuropa,
               'all_melhoresAssistencias': all_melhoresAssistencias, 'all_videodasemana': all_videodasemana
               }
    return render(request, 'futebol/index.html', context)

def noticia(request):
    all_noticias = Noticia.objects.all().order_by('-id')[:10]
    context = {'all_noticias': all_noticias}
    return render(request, 'futebol/noticia.html', context)

def about(request):
    return render(request, 'futebol/about.html')

def contactos(request):
    return render(request,'futebol/contactos.html')

def clubes(request):
    all_clubes = Clube.objects.all()
    context = {'all_clubes': all_clubes}
    return render(request, 'futebol/clubes.html', context)

def agenda(request):
    all_clubes = Clube.objects.all()
    all_quartos = JogosRecentesLigaCampeoes.objects.all().order_by('-id')[2:6]
    all_meias = JogosRecentesLigaCampeoes.objects.all().order_by('-id')[:2]
    all_ultimajornada = JogosRecentesLigaPortuguesa.objects.all().order_by('-id')[:4]
    all_penultimajornada = JogosRecentesLigaPortuguesa.objects.all().order_by('-id')[4:8]
    context = {'all_quartos': all_quartos, 'all_clubes': all_clubes, 'all_meias': all_meias, 'all_ultimajornada':all_ultimajornada,
               'all_penultimajornada':all_penultimajornada}
    return render(request, 'futebol/agenda.html', context)

def estatisticas(request):
    all_classificacao = classificacao.objects.all().order_by('-pontos')
    all_clubes = Clube.objects.all()
    all_melhoresPortugal = MelhoresMarcadoresPortugal.objects.all().order_by('-pontos')[:3]
    all_melhoresEuropa = MelhoresMarcadoresEuropa.objects.all().order_by('-pontos')[:3]
    all_melhoresAssistencias = MelhoresAssistencias.objects.all().order_by('-pontos')[:3]
    context = {'all_clubes': all_clubes, 'all_melhoresPortugal': all_melhoresPortugal, 'all_melhoresEuropa': all_melhoresEuropa,
               'all_melhoresAssistencias': all_melhoresAssistencias, 'all_classificacao': all_classificacao}
    return render(request, 'futebol/estatisticas.html', context)

def detail(request, noticia_id):
    detalhe = Noticia.objects.get(pk=noticia_id)
    content_type = ContentType.objects.get_for_model(Noticia)
    obj_id = noticia_id
    comentarios = Comment.objects.filter(content_type=content_type, object_id =obj_id).order_by('-timestamp')
    initial_data = {
        "content_type": content_type,
        "object_id": noticia_id
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    if form.is_valid() and request.user.is_authenticaated():
        c_type = form.cleaned_data.get("content_type")
        conteudo = ContentType.objects.get(model= c_type)
        obje_id = form.cleaned_data.get("object_id")
        content_data = form.cleaned_data.get("content")
        new_comment, created = Comment.objects.get_or_create(
                                user = request.user,
                                content_type = conteudo,
                                object_id = obje_id,
                                content = content_data
        )
    return render(request, 'futebol/especifico.html',{'noticia': detalhe, 'comentarios':comentarios, 'comment_form':form})

def detailClube(request, clube_id):
    clube = Clube.objects.get(pk=clube_id)
    return render(request, 'futebol/clube_especifico.html', {'clube': clube})


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/futebol")

    return render(request, 'futebol/form.html', {"form": form, "title": title})


def register_view(request):
    title = "Registo"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/futebol")
    context = {"form": form,
               "title": title
    }
    return render(request, "futebol/form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/futebol")
