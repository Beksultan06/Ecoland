# Generated by Django 5.1.3 on 2024-12-11 10:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("destinations", "0004_remove_destinationsdetailmodels_descriptions_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="DestinationsPynkt",
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
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="Активен?"),
                ),
            ],
            options={
                "verbose_name_plural": "Пункты наших направления",
            },
        ),
    ]
