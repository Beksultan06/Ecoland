from django.db import models
from ckeditor.fields import RichTextField

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

class NewsListDetails(models.Model):
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
    descriptions = RichTextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Лист Новостей'

class NewsComment(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    email = models.EmailField(
        verbose_name='Электронная почта'
    )
    comment = models.TextField(
        verbose_name='Описание'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание коментарий',
        null=True,
        blank=True
    )
    news = models.ForeignKey(NewsListDetails, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Комментрия Новостей'
        ordering = ['-created_at']