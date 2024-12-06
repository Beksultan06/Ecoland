# Generated by Django 5.1.3 on 2024-12-05 04:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SettingsBanner",
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
                ("title", models.CharField(max_length=155, verbose_name="Заголовка")),
                (
                    "descriptions",
                    ckeditor.fields.RichTextField(verbose_name="Описание"),
                ),
                ("image", models.ImageField(upload_to="settings", verbose_name="Фото")),
            ],
            options={
                "verbose_name_plural": "Настройка Главной страницы",
            },
        ),
        migrations.AlterModelOptions(
            name="settings",
            options={},
        ),
        migrations.RemoveField(
            model_name="settings",
            name="descriptions",
        ),
        migrations.RemoveField(
            model_name="settings",
            name="image",
        ),
        migrations.AddField(
            model_name="settings",
            name="descriptipons_plan",
            field=ckeditor.fields.RichTextField(
                default=1, verbose_name="Описание плана"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="image_plan",
            field=models.ImageField(
                default=1, upload_to="settingsplan", verbose_name="Фото плана"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="title2",
            field=models.CharField(
                default=1, max_length=155, verbose_name="Заголовка - 2"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="title_plan_1",
            field=models.CharField(
                default=1, max_length=155, verbose_name="Заголовка Плана"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="title_plan_2",
            field=models.CharField(
                default=1, max_length=155, verbose_name="Заголовка Плана 2"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="title_tours",
            field=models.CharField(
                default=1, max_length=155, verbose_name="Заголовка Туров"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="settings",
            name="title_tours2",
            field=models.CharField(
                default=1, max_length=155, verbose_name="Заголовка Туров 2"
            ),
            preserve_default=False,
        ),
    ]