from django.db import models

# Create your models here.
class NewsPage(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    image = models.ImageField(
        upload_to='news/',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Строница Новостей'

class NewsList(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    image = models.ImageField(
        upload_to='news/details',
        verbose_name='Фото'
    )
    day = models.IntegerField(
        verbose_name = 'День'
    )
    month = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Лист Новостей'