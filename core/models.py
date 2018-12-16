from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name='제목',
    )
    content1 = models.TextField(verbose_name='문단1')
    content2 = models.TextField(verbose_name='문단2', blank=True, null=True)
    content3 = models.TextField(verbose_name='문단3', blank=True, null=True)
    map = models.TextField(verbose_name='지도', blank=True, null=True)
    graph = models.TextField(verbose_name='그래프', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{0}.{1}'.format(self.pk, self.title)

    def get_absolute_url(self):
        return reverse('core:article_detail', kwargs={
            'pk': self.pk,
        })
