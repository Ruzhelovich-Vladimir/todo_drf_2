from uuid import uuid4

from django.db import models

from authors.models import Author


class Project(models.Model):
    """ Проекты """
    uid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    name = models.CharField(verbose_name='имя', max_length=64)
    project_manager = models.ForeignKey(Author,
                                       verbose_name='менеджер проекта',
                                       on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(verbose_name='создано',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлено', auto_now=True)

    def __str__(self):
       return self.name


class Development(models.Model):
    """ Разработчики """

    uid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    project = models.ForeignKey(Project,
                               verbose_name='проект',
                               on_delete=models.DO_NOTHING)
    development = models.ForeignKey(Author,
                                verbose_name='разработчик',
                                on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(verbose_name='создано',
                                      auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлено', auto_now=True)
