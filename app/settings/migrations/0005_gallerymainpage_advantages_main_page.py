# Generated by Django 5.1.3 on 2024-12-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0004_gallerymainpage"),
    ]

    operations = [
        migrations.AddField(
            model_name="gallerymainpage",
            name="advantages_main_page",
            field=models.CharField(
                default=1, max_length=155, verbose_name="Наши примущество"
            ),
            preserve_default=False,
        ),
    ]
