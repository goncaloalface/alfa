# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-08 10:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='classificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clube', models.CharField(max_length=100)),
                ('imagem', models.CharField(max_length=100)),
                ('pontos', models.CharField(max_length=100)),
                ('jogos', models.CharField(max_length=100)),
                ('vitorias', models.CharField(max_length=100)),
                ('empates', models.CharField(max_length=100)),
                ('derrotas', models.CharField(max_length=100)),
                ('golos_marcados', models.IntegerField()),
                ('golos_sofridos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=10)),
                ('imagem', models.CharField(max_length=2000)),
                ('historia', models.CharField(max_length=5000)),
                ('wiki', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JogosRecentesLigaCampeoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EquipaDaCasa', models.CharField(max_length=100)),
                ('resultado', models.CharField(max_length=6)),
                ('EquipaDaFora', models.CharField(max_length=100)),
                ('ImagemDaCasa30x30', models.CharField(max_length=2000)),
                ('ImagemDaFora30x30', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='JogosRecentesLigaPortuguesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EquipaDaCasa', models.CharField(max_length=100)),
                ('resultado', models.CharField(max_length=6)),
                ('EquipaDaFora', models.CharField(max_length=100)),
                ('ImagemDaCasa30x30', models.CharField(max_length=2000)),
                ('ImagemDaFora30x30', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='MelhoresAssistencias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('clube', models.CharField(max_length=100)),
                ('pontos', models.CharField(max_length=100)),
                ('texto', models.CharField(max_length=1000)),
                ('imagem', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='MelhoresMarcadoresEuropa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('clube', models.CharField(max_length=100)),
                ('pontos', models.CharField(max_length=100)),
                ('texto', models.CharField(max_length=1000)),
                ('imagem', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='MelhoresMarcadoresPortugal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('clube', models.CharField(max_length=100)),
                ('pontos', models.CharField(max_length=100)),
                ('texto', models.CharField(max_length=1000)),
                ('imagem', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('texto', models.CharField(max_length=3000)),
                ('autor', models.CharField(max_length=50)),
                ('imagem', models.CharField(max_length=2000)),
                ('breve', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='videodasemana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=4000)),
                ('texto', models.CharField(max_length=3000)),
            ],
        ),
    ]