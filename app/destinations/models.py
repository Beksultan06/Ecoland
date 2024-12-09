from django.db import models

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

# class