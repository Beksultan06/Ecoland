# Generated by Django 5.1.3 on 2024-12-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0006_alter_newscomment_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newscomment",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Дата создание коментарий"
            ),
        ),
    ]
