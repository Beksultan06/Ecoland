# Generated by Django 5.1.3 on 2024-12-06 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0016_contactpage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Form",
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
                ("name", models.CharField(max_length=155, verbose_name="Имя")),
                ("email", models.EmailField(max_length=254, verbose_name="Почты")),
                ("message", models.TextField(verbose_name="Сообщение")),
            ],
            options={
                "verbose_name_plural": "Форма обратного связи",
            },
        ),
    ]