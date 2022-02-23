from uuid import uuid4

from django.db import models


class Author(models.Model):

   uid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
   first_name = models.CharField(verbose_name='имя', max_length=64)
   last_name = models.CharField(verbose_name='фамилия', max_length=64)
   birthday = models.DateField(verbose_name='дата рождения', null=True, blank=True)
   created_at = models.DateTimeField(verbose_name='создано', auto_now_add=True)
   updated_at = models.DateTimeField(verbose_name='обновлено', auto_now=True)

   def __str__(self):
      return f'{self.first_name} {self.last_name}'
