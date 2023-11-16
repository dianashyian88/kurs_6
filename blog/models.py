from django.db import models
from config.settings import AUTH_USER_MODEL
from distribution.models import NULLABLE


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='наименование')
    body = models.TextField(verbose_name='текст статьи')
    image = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    public_date = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ('id',)


