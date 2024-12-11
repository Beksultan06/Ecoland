from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class DestinationsModels(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    image = models.ImageField(
        upload_to='destinations',
        verbose_name='Фото'
    )
    descriptions = RichTextField(
        verbose_name='Описание В деталей'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Наши направление'

class DestinationsDetailModels(models.Model):
    destination = models.ForeignKey(
        DestinationsModels,
        on_delete=models.CASCADE,
        verbose_name='Направление'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Детально о наших направлениях'

class DestinationsPynkt(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Активен?'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Пункты наших направления'