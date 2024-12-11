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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Наши направление'

class DestinationsDetailModels(models.Model):
    destination = models.ForeignKey(
        DestinationsModels,
        on_delete=models.CASCADE,
        verbose_name='Направление'
    )  # Связь с основной моделью
    descriptions = RichTextField(
        verbose_name='Описание'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    title_price = models.IntegerField(
        verbose_name='Заголовка Цены'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Детально о наших направлениях'