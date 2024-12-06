# Generated by Django 5.1.3 on 2024-12-06 06:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0012_aboutpage_image2"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutPercent",
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
                ("procent", models.IntegerField(verbose_name="Проценты")),
            ],
            options={
                "verbose_name_plural": "Проценты о нас ",
            },
        ),
    ]