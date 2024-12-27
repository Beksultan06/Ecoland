from django.db import models
from ckeditor.fields import RichTextField

class Tour(models.Model):
    title = models.CharField(max_length=155,verbose_name='Заголовка')
    image = models.ImageField(upload_to='tour', verbose_name='Фото')
    price = models.IntegerField(verbose_name='Цена')
    person = models.CharField(max_length=155,verbose_name='Цена за человека')
    star = models.CharField(max_length=50,verbose_name='Звезда')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Лист Туров"

class Settings(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовка Туров')
    image = models.ImageField(upload_to='tour', verbose_name='Фото')
    main = models.CharField(max_length=155,verbose_name='Заголовка Главной страницы')
    tour = models.CharField(max_length=155,verbose_name='Туры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Страница туров'

