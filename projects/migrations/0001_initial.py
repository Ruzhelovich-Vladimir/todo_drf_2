# Generated by Django 3.2.12 on 2022-02-23 18:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0002_auto_20220223_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ид')),
                ('name', models.CharField(max_length=64, verbose_name='имя')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='обновлено')),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authors.author', verbose_name='менеджер проекта')),
            ],
        ),
        migrations.CreateModel(
            name='Development',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='ид')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='обновлено')),
                ('development', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='authors.author', verbose_name='разработчик')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.project', verbose_name='проект')),
            ],
        ),
    ]
