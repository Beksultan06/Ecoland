# Generated by Django 5.1.3 on 2024-12-11 11:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0008_newscomment_news"),
    ]

    operations = [
        migrations.AddField(
            model_name="newslistdetails",
            name="descriptions_en",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="Описание"),
        ),
        migrations.AddField(
            model_name="newslistdetails",
            name="descriptions_ru",
            field=ckeditor.fields.RichTextField(null=True, verbose_name="Описание"),
        ),
        migrations.AddField(
            model_name="newslistdetails",
            name="month_en",
            field=models.CharField(max_length=155, null=True, verbose_name="Заголовка"),
        ),
        migrations.AddField(
            model_name="newslistdetails",
            name="month_ru",
            field=models.CharField(max_length=155, null=True, verbose_name="Заголовка"),
        ),
        migrations.AddField(
            model_name="newslistdetails",
            name="title_en",
            field=models.CharField(max_length=155, null=True, verbose_name="Заголовка"),
        ),
        migrations.AddField(
            model_name="newslistdetails",
            name="title_ru",
            field=models.CharField(max_length=155, null=True, verbose_name="Заголовка"),
        ),
        migrations.AddField(
            model_name="newspage",
            name="title_en",
            field=models.CharField(max_length=155, null=True, verbose_name="Заголовка"),
        ),
        migrations.AddField(
            model_name="newspage",
            name="title_ru",
            field=models.CharField(max_length=155, null=True, verbose_name="Заголовка"),
        ),
    ]
