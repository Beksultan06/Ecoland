# Generated by Django 5.1.3 on 2024-12-10 13:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_newslistdetails_delete_newslist"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsComment",
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
                ("descriptions", models.TextField(verbose_name="Описание")),
            ],
            options={
                "verbose_name_plural": "Комментрия Новостей",
            },
        ),
    ]
