# Generated by Django 5.1.3 on 2024-12-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0007_videomainpage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Partners",
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
                    models.ImageField(
                        upload_to="partners/", verbose_name="Лого парнетров"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Наши Партнеры",
            },
        ),
    ]
