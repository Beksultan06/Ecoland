# Generated by Django 5.1.3 on 2024-12-05 10:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0005_gallerymainpage_advantages_main_page"),
    ]

    operations = [
        migrations.CreateModel(
            name="MainTours",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="main/tours/", verbose_name="Фото"),
                ),
                (
                    "superb",
                    models.CharField(max_length=155, verbose_name="превосходно"),
                ),
                ("title", models.CharField(max_length=155, verbose_name="Заголовка")),
                ("price", models.IntegerField(verbose_name="Цена")),
                (
                    "name_city",
                    models.CharField(max_length=155, verbose_name="Название города"),
                ),
            ],
            options={
                "verbose_name_plural": "Туры В Главной странице",
            },
        ),
    ]
