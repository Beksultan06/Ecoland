from django.db import models
from ckeditor.fields import RichTextField

class SettingsBanner(models.Model):
    class Meta:
        verbose_name_plural = 'Настройка Главной страницы Баннера'

    title = models.CharField(max_length=155, verbose_name='Заголовка')
    descriptions = RichTextField(verbose_name='Описание')
    image = models.ImageField(upload_to='settings', verbose_name='Фото')

    def __str__(self):
        return self.title

class Settings(models.Model):
    class Meta:
        verbose_name_plural = 'Настройки Главной Страницы'

    title = models.CharField(max_length=155, verbose_name='Заголовка')
    title2 = models.CharField(max_length=155, verbose_name='Заголовка - 2')
    title_plan_1 = models.CharField(max_length=155, verbose_name='Заголовка Плана')
    title_plan_2 = models.CharField(max_length=155, verbose_name='Заголовка Плана 2')
    descriptions_plan = RichTextField(verbose_name='Описание плана')
    image_plan = models.ImageField(upload_to='settingsplan', verbose_name='Фото плана')
    title_tours = models.CharField(max_length=155, verbose_name='Заголовка Туров')
    title_tours2 = models.CharField(max_length=155, verbose_name='Заголовка Туров 2')
    title_tevily = models.CharField(max_length=155, verbose_name='Заголовка Тевили')
    title_tevily2 = models.CharField(max_length=155, verbose_name='Заголовка Тевили 2')
    video_tevily = models.URLField(verbose_name='Ссылка на видео')
    title_partners = models.CharField(max_length=155, verbose_name='Заголовка Партнеров')
    title_testimonials = models.CharField(max_length=155, verbose_name='Заголовка Отзывов')
    title_testimonials2 = models.CharField(max_length=155, verbose_name='Заголовка Отзывов 2')
    title_choices = models.CharField(max_length=155, verbose_name='Заголовка Выбора')
    title_choices2 = models.CharField(max_length=155, verbose_name='Заголовка Выбора 2')
    descriptions_choices = RichTextField(verbose_name='Описание выбора')
    image_choices = models.ImageField(upload_to='settings', verbose_name='Фото Выбора')
    title_news = models.CharField(max_length=155, verbose_name='Заголовка Новостей')
    title_news2 = models.CharField(max_length=155, verbose_name='Заголовка Новостей 2')

class GalleryMainPage(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовка')
    image = models.ImageField(upload_to='Фото')
    advantages_main_page = models.CharField(max_length=155, verbose_name='Наши примущество')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Галлерия на Главной страницы'

class MainTours(models.Model):
    image = models.ImageField(upload_to='main/tours/', verbose_name='Фото')
    superb = models.CharField(max_length=155, verbose_name='превосходно')
    title = models.CharField(max_length=155, verbose_name='Заголовка')
    price = models.IntegerField(verbose_name='Цена')
    name_city = models.CharField(max_length=155, verbose_name='Название города')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Туры В Главной странице'

class VideoMainPage(models.Model):
    ICON = (
        ("Дикая природаТуры", "Дикая природаТуры"),
        ("Парапланерные туры", "Парапланерные туры"),
        ("Приключенческие туры", "Приключенческие туры"),
        ("Дельтапланерные туры", "Дельтапланерные туры"),
    )

    title = models.CharField(max_length=155, verbose_name='Заголовка')
    icon = models.CharField(max_length=155, verbose_name='Иконка', choices=ICON)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Видео на Главной странице'

class Partners(models.Model):
    image = models.ImageField(upload_to='partners/', verbose_name='Лого парнетров')

    class Meta:
        verbose_name_plural = 'Наши Партнеры'

class ImageMainPage(models.Model):
    image = models.ImageField(upload_to='Фото')

    class Meta:
        verbose_name_plural = 'Фото На Главной Странице'

class DopInfo(models.Model):
    ICON = (
        ("Профессиональный и сертифицированный", "Профессиональный и сертифицированный"),
        ("Получите мгновенное бронирование туров", "Получите мгновенное бронирование туров"),
    )

    title = models.CharField(max_length=155, verbose_name='Заголовка')
    descriptions = RichTextField(verbose_name='Описание')
    icon = models.CharField(max_length=155, verbose_name='Иконка', choices=ICON)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Допольнительная Информация'

class AboutPage(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовка')
    image = models.ImageField(upload_to='about', verbose_name='Фото')
    title_tevily = models.CharField(max_length=155, verbose_name='Заголовка tevily')
    title_tevily2 = models.CharField(max_length=155, verbose_name='Заголовка tevily 2')
    title_tevily3 = models.CharField(max_length=155, verbose_name='Заголовка tevily 3')
    descriptions = RichTextField(verbose_name='Описание tevily')
    image2 = models.ImageField(upload_to='about', verbose_name='Фото')
    title_ready = models.CharField(max_length=155, verbose_name='Заголовка Готовый')
    title_ready2 = models.CharField(max_length=155, verbose_name='Заголовка Готовый 2')
    title_saying = models.CharField(max_length=155, verbose_name='Заголовка Говоря')
    title_saying2 = models.CharField(max_length=155, verbose_name='Заголовка Говоря 2')
    title_video = models.CharField(max_length=155, verbose_name='Заголовка Видио')
    title_video2 = models.CharField(max_length=155, verbose_name='Заголовка Видио 2')
    video = models.URLField(verbose_name='Ссылка на видео')
    title_team = models.CharField(max_length=155, verbose_name='Заголовка команды')
    title_team2 = models.CharField(max_length=155, verbose_name='Заголовка команды 2')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Настройки Страницы О нас'

class AboutPercent(models.Model):
    class Meta:
        verbose_name_plural = 'Проценты (о нас )'

    title = models.CharField(max_length=155, verbose_name='Заголовка')
    procent = models.IntegerField(verbose_name='Проценты')

    def __str__(self):
        return self.title

class TeamAboutPage(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовка')
    job_title = models.CharField(max_length=155, verbose_name='Должность')
    image = models.ImageField(upload_to='team_about', verbose_name='Фото')
    fb = models.URLField(verbose_name='Facebook', blank=True, null=True)
    inst = models.URLField(verbose_name='Instagram', blank=True, null=True)
    twitter = models.URLField(verbose_name='Твиттер', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Наша команда (Страница О нас)'

class ContactPage(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовка')
    image = models.ImageField(upload_to='contact', verbose_name='Фото на баннаре')
    title_form = models.CharField(max_length=155, verbose_name='Заголовка Формы')
    title_form2 = models.CharField(max_length=155, verbose_name='Заголовка Формы 2')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Настройка Страницы Конатакты'

class Form(models.Model):
    name = models.CharField(max_length=155, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Форма на страницах'
