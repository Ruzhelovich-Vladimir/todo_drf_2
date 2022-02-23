from uuid import uuid4

from django.db import models

from authors.models import Author
from projects.models import Project


class Node(models.Model):
    """ Заметки """
    STATUS = [
        ('N', 'Новый'),
        ('P', 'В процессе'),
        ('S', 'Отложен'),
        ('D', 'Выполнено')
    ]

    uid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    project = models.ForeignKey(Project,
                                verbose_name='проект',
                                on_delete=models.DO_NOTHING)
    text = models.TextField(verbose_name='заметка',  max_length=1000)
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.DO_NOTHING)
    status = models.CharField(choices=STATUS, max_length=1)
    created_at = models.DateTimeField(verbose_name='создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлено', auto_now=True)
